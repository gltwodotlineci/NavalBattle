from string import ascii_uppercase as letters

class Attack:
    def __init__(self, grid, coordinates, grid_dim):
        self.grid = grid
        self.coordinates = coordinates
        self.grid_dim = grid_dim

    def result_attack(self):
        if self.grid[self.coordinates[0]][self.coordinates[1]] == "(:)":
            self.grid[self.coordinates[0]][self.coordinates[1]] = "-No"
        else:
            self.grid[self.coordinates[0]][self.coordinates[1]] = "[#]"
        a_f = list(letters[:self.grid_dim])
        num = iter(range(1,(self.grid_dim+1)))
        print("     " + "   ".join(a_f))
        for row in self.grid:
            print(" ", next(num), end = " ")
            print(" ".join(row))

        return self.grid
