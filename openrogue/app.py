try:
    import pyxel
except Exception:  # pragma: no cover - fallback for missing dependency
    from .pyxel_stub import pyxel

from .map import Map
from .score import ScoreManager
from .resources import open_editor, load_table, save_table

from .map import Map

# Mapping of movement keys and gamepad buttons
_KEY_LEFT = pyxel.KEY_LEFT
_KEY_RIGHT = pyxel.KEY_RIGHT
_KEY_UP = pyxel.KEY_UP
_KEY_DOWN = pyxel.KEY_DOWN
_KEY_MONSTER_EDIT = pyxel.KEY_M
_KEY_ITEM_EDIT = pyxel.KEY_I
_KEY_MONSTER_PARAM = pyxel.KEY_P
_KEY_ITEM_PARAM = pyxel.KEY_O

_BTN_LEFT = pyxel.GAMEPAD1_BUTTON_DPAD_LEFT
_BTN_RIGHT = pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT
_BTN_UP = pyxel.GAMEPAD1_BUTTON_DPAD_UP
_BTN_DOWN = pyxel.GAMEPAD1_BUTTON_DPAD_DOWN

class OpenRogue:
    def __init__(self):
        try:
            pyxel.init(160, 120, title="OpenRogue")
        except BaseException:
            from .pyxel_stub import pyxel as stub
            globals().update(pyxel=stub)
            global _KEY_LEFT, _KEY_RIGHT, _KEY_UP, _KEY_DOWN
            global _KEY_MONSTER_EDIT, _KEY_ITEM_EDIT
            global _KEY_MONSTER_PARAM, _KEY_ITEM_PARAM
            global _BTN_LEFT, _BTN_RIGHT, _BTN_UP, _BTN_DOWN
            _KEY_LEFT = pyxel.KEY_LEFT
            _KEY_RIGHT = pyxel.KEY_RIGHT
            _KEY_UP = pyxel.KEY_UP
            _KEY_DOWN = pyxel.KEY_DOWN
            _KEY_MONSTER_EDIT = pyxel.KEY_M
            _KEY_ITEM_EDIT = pyxel.KEY_I
            _KEY_MONSTER_PARAM = pyxel.KEY_P
            _KEY_ITEM_PARAM = pyxel.KEY_O
            _BTN_LEFT = pyxel.GAMEPAD1_BUTTON_DPAD_LEFT
            _BTN_RIGHT = pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT
            _BTN_UP = pyxel.GAMEPAD1_BUTTON_DPAD_UP
            _BTN_DOWN = pyxel.GAMEPAD1_BUTTON_DPAD_DOWN
            pyxel.init(160, 120, title="OpenRogue")

        self.map = Map(20, 15)
        self.x, self.y = self.map.start_pos
        self.moves = 0
        self.scores = ScoreManager()
        self.edit_mode = None
        self.edit_data = []
        self.edit_index = 0

    def update(self):
        if self.edit_mode:
            if pyxel.btnp(pyxel.KEY_Q):
                save_table(self.edit_mode, self.edit_data)
                self.edit_mode = None
                return
            if pyxel.btnp(_KEY_UP):
                self.edit_index = (self.edit_index - 1) % len(self.edit_data)
            if pyxel.btnp(_KEY_DOWN):
                self.edit_index = (self.edit_index + 1) % len(self.edit_data)
            if self.edit_data:
                current = self.edit_data[self.edit_index]
                if self.edit_mode == "monsters":
                    if pyxel.btnp(_KEY_LEFT):
                        current["hp"] = max(1, current.get("hp", 1) - 1)
                    if pyxel.btnp(_KEY_RIGHT):
                        current["hp"] = current.get("hp", 1) + 1
                elif self.edit_mode == "items":
                    if pyxel.btnp(_KEY_LEFT) or pyxel.btnp(_KEY_RIGHT):
                        current["effect"] = "spell" if current.get("effect") == "heal" else "heal"
            return

        if pyxel.btnp(pyxel.KEY_Q):
            self.scores.add_score(self.moves)
            pyxel.quit()

        if pyxel.btnp(_KEY_MONSTER_EDIT):
            open_editor("monsters.pyxres")

        if pyxel.btnp(_KEY_ITEM_EDIT):
            open_editor("items.pyxres")

        if pyxel.btnp(_KEY_MONSTER_PARAM):
            self.edit_mode = "monsters"
            self.edit_data = load_table("monsters")
            self.edit_index = 0
            return

        if pyxel.btnp(_KEY_ITEM_PARAM):
            self.edit_mode = "items"
            self.edit_data = load_table("items")
            self.edit_index = 0
            return

        dx = dy = 0

        if pyxel.btn(_KEY_LEFT) or pyxel.btn(_BTN_LEFT):
            dx = -1
        if pyxel.btn(_KEY_RIGHT) or pyxel.btn(_BTN_RIGHT):
            dx = 1
        if pyxel.btn(_KEY_UP) or pyxel.btn(_BTN_UP):
            dy = -1
        if pyxel.btn(_KEY_DOWN) or pyxel.btn(_BTN_DOWN):
            dy = 1

        new_x = self.x + dx
        new_y = self.y + dy
        if self.map.is_walkable(new_x, new_y):
            if new_x != self.x or new_y != self.y:
                self.moves += 1
            self.x = new_x
            self.y = new_y

    def draw(self):
        pyxel.cls(0)

        if self.edit_mode:
            pyxel.text(2, 2, f"Editing {self.edit_mode} - Q to save", 7)
            for i, entry in enumerate(self.edit_data):
                marker = ">" if i == self.edit_index else " "
                if self.edit_mode == "monsters":
                    line = f"{marker} {entry.get('name')} HP:{entry.get('hp')}"
                else:
                    line = f"{marker} {entry.get('name')} {entry.get('effect')}"
                pyxel.text(2, 12 + i * 8, line, 7)
            return

        for y, row in enumerate(self.map.tiles):
            for x, tile in enumerate(row):
                if tile == "#":
                    pyxel.rect(x * 8, y * 8, 8, 8, 5)

        best = self.scores.best_score()
        if best:
            pyxel.text(2, 2, f"Best: {best['moves']} moves", 7)

        pyxel.text(self.x * 8 + 2, self.y * 8 + 2, "@", 11)

    def run(self):
        pyxel.run(self.update, self.draw)
