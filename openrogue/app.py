import pyxel

class OpenRogue:
    def __init__(self):
        # "caption" is deprecated; use "title" for window text
        pyxel.init(160, 120, title="OpenRogue")

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 50, "Hello, OpenRogue!", pyxel.frame_count % 16)

    def run(self):
        pyxel.run(self.update, self.draw)
