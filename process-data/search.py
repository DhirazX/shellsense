import re
import sqlite3
from pathlib import Path
from rank_bm25 import BM25Okapi

DB_PATH = Path("data/howto.db")

# Fetch data from the database
def fetch_data():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    try:
        rows = conn.execute("SELECT id, command, page_desc, ex_desc, ex_cmd from examples").fetchall()
    finally:
        conn.close()
    return [dict(r) for r in rows]

# TOkenizer function
def tokenize_dict(data):
    return {
        key: re.findall(r"[a-z0-9]+", value.lower())
        for key, value in data.items()
        if key != "id"
    }

# Build corpus for BM25
def build_corpus():
    rows = fetch_data()
    corpus = []

    for row in rows:
         tokens = tokenize_dict(row)
         corpus.append(tokens)

    # "corups" here is: List of dicts of List
    # {'command': ['zypper'], 'ex_desc': ['install', 'a', 'new', 'package'], 'ex_cmd': [...], ...}
    # BM25 expects a List of List or a flat list
    # Like this ['zypper', 'install', 'a', 'new', 'package', ...]

    flat_corpus = []

    for c in corpus:
        tokens =[]
        for v in c.values():
            tokens.extend(v)
            flat_corpus.append(tokens)

    return flat_corpus    



if __name__ == "__main__":
    build_corpus()

