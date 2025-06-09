class Map:
    """Simple grid-based map."""

    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.tiles = self._generate()
        self.start_pos = (1, 1)

    def _generate(self):
        tiles = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1:
                    row.append("#")
                else:
                    row.append(".")
            tiles.append(row)
        return tiles

    def is_walkable(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x] != "#"
        return False
