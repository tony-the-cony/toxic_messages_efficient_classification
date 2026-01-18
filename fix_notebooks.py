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
    fixed_any = False
    for nb_path in NOTEBOOKS:
        fixed_any |= fix_notebook(nb_path)

    if fixed_any:
        print("Some notebooks were fixed. Please commit the changes.")
        sys.exit(1)  # Fail CI to prompt a commit
    else:
        print("All notebooks are clean.")

if __name__ == "__main__":
    main()