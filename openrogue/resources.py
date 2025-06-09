import json
from pathlib import Path


ASSET_DIR = Path(__file__).resolve().parent.parent / "resources"


def load_table(name: str):
    path = ASSET_DIR / f"{name}.json"
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def open_editor(resource: str):
    """Open the Pyxel resource editor for the given file."""
    try:
        import pyxel
        pyxel.tools.editor.run(str(ASSET_DIR / resource))
    except Exception:
        print(f"Cannot open editor for {resource}")


def save_table(name: str, data):
    path = ASSET_DIR / f"{name}.json"
    try:
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except OSError:
        print(f"Cannot save {name}.json")

