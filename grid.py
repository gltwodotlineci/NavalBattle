class Grid:
    def __init__(self, width):
        self.width = width

    def create_grid(self):
        return [['(:)'] * self.width for i in range(self.width)]