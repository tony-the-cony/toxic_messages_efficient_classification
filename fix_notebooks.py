#!/usr/bin/env python3
import json
import pathlib

NOTEBOOK_DIR = pathlib.Path(".")  # root of repo
NOTEBOOKS = list(NOTEBOOK_DIR.glob("**/*.ipynb"))

def remove_widgets(d):
    """Recursively remove 'widgets' key from dictionaries."""
    if isinstance(d, dict):
        if "widgets" in d:
            del d["widgets"]
        for v in d.values():
            remove_widgets(v)
    elif isinstance(d, list):
        for item in d:
            remove_widgets(item)

def fix_notebook(path: pathlib.Path):
    with path.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    remove_widgets(nb)

    with path.open("w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)
    print(f"Fixed: {path}")

def main():
    for nb_path in NOTEBOOKS:
        fix_notebook(nb_path)
    print("All notebooks fixed (widgets removed).")

if __name__ == "__main__":
    main()