import pyxel

from .map import Map

# Mapping of movement keys and gamepad buttons
_KEY_LEFT = pyxel.KEY_LEFT
_KEY_RIGHT = pyxel.KEY_RIGHT
_KEY_UP = pyxel.KEY_UP
_KEY_DOWN = pyxel.KEY_DOWN

_BTN_LEFT = pyxel.GAMEPAD1_BUTTON_DPAD_LEFT
_BTN_RIGHT = pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT
_BTN_UP = pyxel.GAMEPAD1_BUTTON_DPAD_UP
_BTN_DOWN = pyxel.GAMEPAD1_BUTTON_DPAD_DOWN

class OpenRogue:
    def __init__(self):
        pyxel.init(160, 120, title="OpenRogue")

        self.map = Map(20, 15)
        self.x, self.y = self.map.start_pos

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

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
            self.x = new_x
            self.y = new_y

    def draw(self):
        pyxel.cls(0)

        for y, row in enumerate(self.map.tiles):
            for x, tile in enumerate(row):
                if tile == "#":
                    pyxel.rect(x * 8, y * 8, 8, 8, 5)

        pyxel.text(self.x * 8 + 2, self.y * 8 + 2, "@", 11)

    def run(self):
        pyxel.run(self.update, self.draw)
