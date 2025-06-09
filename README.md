# OpenRogue

An open-source roguelike game built with Pyxel. Add your own monsters, items, and more — and help us expand a world full of infinite adventure.

## Project layout

```
openrogue/
    __init__.py
    app.py
main.py
```

The `openrogue` package holds the game code, and `main.py` launches a minimal window using Pyxel.

## Running locally

Install the dependency and start the demo:

```bash
pip install pyxel
python main.py
```

Press `Q` to quit the window.

Use the arrow keys or a connected gamepad's d-pad to move the `@` character around the screen.

The demo now includes a basic grid-based map. `#` tiles are impassable walls while `.` tiles are floor. Your character starts inside the room and cannot walk through walls.
