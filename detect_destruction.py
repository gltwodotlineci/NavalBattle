from ship import Ship

class DetectDestrutedShip:
    def __init__(self, playr_name, player_grid):
        self.player_name = playr_name
        self.player_gride = player_grid
    def check(self,coord_h):
        limit = 3
        player_h = coord_h[self.player_name]
        for k in range(1,3):
            if player_h['horizontal'][k] == 1:
                count_horizontal = 0
                for j in range(player_h['ship_start'][k-1],player_h['ship_start'][k*2]+1):
                    # checking the state of the ship.
                    if self.player_gride[player_h['ship_start'][0]][j] != "\033[1;32;40m[O]":
                        count_horizontal = count_horizontal + 1
                    if count_horizontal == k*2+1:
                        print("The ship number "+k+ " has been destroyed!")
            else:
                count_vertical = 0
                for k in range((['ship_start'][0]),['ship_start'][k*2]+1):
                    # checking the state of the ship.
                    if self.player_gride[k][player_h['end_ship'][1]] != "\033[1;32;40m[O]":
                        count_vertical = count_vertical + 1
                    if  count_vertical == (k*2 +1):
                        print("The ship number "+k+ " has been destroyed!")


    def signal_destruction(self):
        pass
