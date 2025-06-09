class PyxelStub:
    KEY_LEFT = 0
    KEY_RIGHT = 1
    KEY_UP = 2
    KEY_DOWN = 3
    KEY_Q = 4
    KEY_M = 5
    KEY_I = 6
    KEY_P = 7
    KEY_O = 8

    GAMEPAD1_BUTTON_DPAD_LEFT = 10
    GAMEPAD1_BUTTON_DPAD_RIGHT = 11
    GAMEPAD1_BUTTON_DPAD_UP = 12
    GAMEPAD1_BUTTON_DPAD_DOWN = 13

    def __init__(self):
        self.width = 0
        self.height = 0

    def init(self, width, height, title="OpenRogue"):
        self.width = width
        self.height = height
        print("[Pyxel stub] init called - no GUI available")

    def btn(self, key):
        return False

    def btnp(self, key):
        return False

    def cls(self, color=0):
        pass

    def rect(self, x, y, w, h, color):
        pass

    def text(self, x, y, txt, color):
        print(txt)

    def quit(self):
        pass

    def run(self, update, draw):
        update()
        draw()


class EditorStub:
    def run(self, path=None):
        print(f"[Pyxel stub] editor open for {path}")


class ToolsStub:
    def __init__(self):
        self.editor = EditorStub()


pyxel = PyxelStub()
pyxel.tools = ToolsStub()
