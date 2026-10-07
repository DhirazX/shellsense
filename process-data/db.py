# Store the tldr pages data we parsed into a database
import sqlite3
from pathlib import Path
from parser import parse_tldr_files

PAGES_DIR = Path("data/tldr/pages")
PLATFORMS = ["common", "linux"]
DB_PATH = Path("data/howto.db")

DB_SCHEMA = """
    CREATE TABLE IF NOT EXISTS examples (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        command TEXT NOT NULL,
        platform TEXT NOT NULL,
        page_desc TEXT,
        ex_desc TEXT NOT NULL,
        ex_cmd TEXT NOT NULL
);
"""

# func to normalize all cmd examples
def collect_records(pages_dir = PAGES_DIR):
    records =[]
    for platform in PLATFORMS:
        for tldr_page in sorted((pages_dir / platform).glob("*.md")):
            try:
                parsed_tldr = parse_tldr_files(tldr_page)
            except Exception as e:
                print(f"Couldnt parse {tldr_page}, {e}")
                continue

            for data in parsed_tldr:
                data["platform"] = platform
            
            records.extend(parsed_tldr)

    return records

def build_db(db_path=DB_PATH):
    records = collect_records()

    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        with conn: 
            conn.execute("DROP TABLE IF EXISTS examples")
            conn.execute(DB_SCHEMA)
            conn.executemany(
                """
                INSERT INTO examples (command, platform, page_desc, ex_desc, ex_cmd)
                VALUES (:command, :platform, :page_desc, :ex_desc, :ex_cmd)
                """,
                records,
            )
    finally:
        conn.close()

    print(f"Num of Records: {len(records)} DB Path: {db_path}")



def load_records(db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute("SELECT * FROM examples").fetchall()
    finally:
        conn.close()
    return [dict(row) for row in rows]


if __name__ == "__main__":
    build_db()