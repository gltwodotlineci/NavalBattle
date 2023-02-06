class Grid:
    def __init__(self, width):
        self.width = width

    def create_grid(self):
        return [['\x1b[34m(:)\x1b[0m'] * self.width for i in range(self.width)]
