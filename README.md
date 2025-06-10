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

## Controls

While the demo is running you can use the following keys (or a gamepad's d‑pad) to play:

- **Arrow keys / d‑pad**: Move the `@` character around the map when not editing. (矢印キー／十字キー：編集していない時に`@`キャラクターを移動)
- **Q**: Quit the game and save your score. When editing parameters, this key saves changes and returns to the game. (Qキー：ゲーム終了とスコア保存、編集中は変更を保存して戻る)
- **M**: Open `monsters.pyxres` in the Pyxel editor to modify monster graphics. (Mキー：Pyxelエディタで`monsters.pyxres`を開きモンスター画像を編集)
- **I**: Open `items.pyxres` in the Pyxel editor to modify item graphics. (Iキー：Pyxelエディタで`items.pyxres`を開きアイテム画像を編集)
- **P**: Edit monster parameters. Use **UP/DOWN** to choose an entry and **LEFT/RIGHT** to adjust its HP. (Pキー：モンスターのパラメータ編集、上下キーで項目選択、左右キーでHP調整)
- **O**: Edit item parameters. Use **UP/DOWN** to choose an entry and **LEFT/RIGHT** to toggle its effect between "heal" and "spell". (Oキー：アイテムのパラメータ編集、上下キーで項目選択、左右キーで効果切替)

If `pyxel` cannot initialize (for example on a headless server), the game falls back to a minimal console mode using a built-in stub. This allows the program to run without opening a window, though no interactive gameplay is available.


The demo now includes a basic grid-based map. `#` tiles are impassable walls while `.` tiles are floor. Your character starts inside the room and cannot walk through walls.

Each run tracks how many moves you make before quitting. Scores are saved to `scores.json` and the best score is shown in the top-left corner of the screen.
