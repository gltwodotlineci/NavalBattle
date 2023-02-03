from string import ascii_uppercase as letters

class Attack:
    def __init__(self, grid, coordinates):
        self.grid = grid
        self.coordinates = coordinates

    def result_attack(self):
        if self.grid[self.coordinates[0]][self.coordinates[1]] == "(:)" or self.grid[self.coordinates[0]][self.coordinates[1]] == "-No":
            self.grid[self.coordinates[0]][self.coordinates[1]] = "-No"
        else:
            self.grid[self.coordinates[0]][self.coordinates[1]] = "[#]"

        return self.grid
