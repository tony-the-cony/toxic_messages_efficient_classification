#!/usr/bin/env python3
import json
import pathlib
import sys

NOTEBOOK_DIR = pathlib.Path(".")  # root of repo
NOTEBOOKS = list(NOTEBOOK_DIR.glob("**/*.ipynb"))

def fix_notebook(path: pathlib.Path):
    with path.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    if "widgets" in nb.get("metadata", {}):
        del nb["metadata"]["widgets"]
        with path.open("w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print(f"Fixed: {path}")
        return True
    return False

def main():
    for nb_path in NOTEBOOKS:
        fix_notebook(nb_path)
    print("All notebooks are fixed (if needed).")

if __name__ == "__main__":
    main()