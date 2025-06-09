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

If `pyxel` cannot initialize (for example on a headless server), the game falls
back to a minimal console mode using a built-in stub. This allows the program to
run without opening a window, though no interactive gameplay is available.

Press `Q` to quit the window.

Press `M` to open the monster texture file in the Pyxel editor, or `I` to open
the item texture file. Editing and saving these `.pyxres` files will let the
game use your updated sprites.

Use the arrow keys or a connected gamepad's d-pad to move the `@` character around the screen.

The demo now includes a basic grid-based map. `#` tiles are impassable walls while `.` tiles are floor. Your character starts inside the room and cannot walk through walls.

Each run tracks how many moves you make before quitting. Scores are saved to `scores.json` and the best score is shown in the top-left corner of the screen.
