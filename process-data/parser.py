# Parse tldr files 
from pathlib import Path

def parse_tldr_files(file_path):
    lines = Path(file_path).read_text(encoding="utf-8").splitlines()

    command = ""
    desc_parts = []
    examples = []    
    ex_desc = ""

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith("# "):
            command = line[2:].strip()
        elif line.startswith(">"):
            if not line.startswith("> More information:" or "> See also:"):
                desc_parts.append(line[1:].strip())
        elif line.startswith("- "):
            ex_desc = line[2:].strip().rstrip(":")
        elif line.startswith("`") and line.endswith("`"):
            if ex_desc:
                examples.append((ex_desc, line[1:-1]))
                ex_desc = "" 

    page_desc = " ".join(desc_parts)

    return [
        {
            "command": command,
            "page_desc": page_desc,
            "ex_desc": desc,
            "ex_cmd": cmd,
        }
        for desc, cmd in examples
    ]
    