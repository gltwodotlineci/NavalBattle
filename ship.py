from interact_conditions import InteractConditions

class Ship:
    def __init__(self, player1, player2, dimention_game):
            self.player1 = player1
            self.player2 = player2
            self.dimention_game = dimention_game
            self.ship_start, self.ship_end  = [], []


    def creat_ship(self, grid):
        if self.ship_start[0] == self.ship_end[0]:
            for j in range(self.ship_start[1],(self.ship_end[1]+1)):
                grid[self.ship_start[0]][j] = "[o]"
        elif self.ship_start[1] == self.ship_end[1]:
            for k in range((self.ship_start[0]),self.ship_end[0]+1):
                grid[k][self.ship_end[1]] = "[o]"
        print("____________________________________")
        return grid


    def create_ships(self,):

        for player in [self.player1, self.player2]:
            print("_____________________")
            print("Hi "+player.name+" you can start creating your three ships")
            print("_____________________")
            for n in range(1,4):
                for i in range(0,2):
                    if i == 0:
                        begining_ship_x =  InteractConditions(player.name, n).coordinate_conditions(self.dimention_game, "of the begining of yur ship "+str(n)+": ")
                        begining_ship_y = InteractConditions(player.name, n).coordinate_conditions(self.dimention_game, "of the begingin of yur ship "+str(n)+": ")
                    else:
                        end_ship_x =  InteractConditions(player.name, n).coordinate_conditions(self.dimention_game, "of the end of yur ship "+str(n)+": ")
                        end_ship_x = InteractConditions(player.name, n).verticla_length(begining_ship_x, end_ship_x)
                        end_ship_y = InteractConditions(player.name, n).coordinate_conditions(self.dimention_game,  "of the end of yur ship "+str(n)+": ")
                        end_ship_y = InteractConditions(player.name, n).ship_conditions(begining_ship_x, begining_ship_y, end_ship_x, end_ship_y)
                self.ship_start.append(begining_ship_x)
                self.ship_start.append(begining_ship_y)
                self.ship_end.append(end_ship_x)
                self.ship_end.append(end_ship_y)

                self.creat_ship(player.grid)
                self.ship_start, self.ship_end = [], []
