class Ship:
    def __init__(self, grid, start_point, end_point):
            self.grid = grid
            self.start_point = start_point
            self.end_point = end_point

    def creat_ship(self):
        if self.start_point[0] == self.end_point[0]:
            for j in range(self.start_point[1],(self.end_point[1]+1)):
                self.grid[self.start_point[0]][j] = "[o]"
        elif self.start_point[1] == self.end_point[1]:
            for k in range((self.start_point[0]),self.end_point[0]+1):
                self.grid[k][self.end_point[1]] = "[o]"
        print("____________________________________")
        return self.grid
