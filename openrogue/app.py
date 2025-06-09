import pyxel


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
        pyxel.init(160, 120, caption="OpenRogue")
        self.x = 72
        self.y = 56

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # Keyboard movement
        if pyxel.btn(_KEY_LEFT) or pyxel.btn(_BTN_LEFT):
            self.x = max(self.x - 1, 0)
        if pyxel.btn(_KEY_RIGHT) or pyxel.btn(_BTN_RIGHT):
            self.x = min(self.x + 1, pyxel.width - 4)
        if pyxel.btn(_KEY_UP) or pyxel.btn(_BTN_UP):
            self.y = max(self.y - 1, 0)
        if pyxel.btn(_KEY_DOWN) or pyxel.btn(_BTN_DOWN):
            self.y = min(self.y + 1, pyxel.height - 8)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(self.x, self.y, "@", 11)

    def run(self):
        pyxel.run(self.update, self.draw)
