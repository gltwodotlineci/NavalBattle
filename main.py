from interact_conditions import InteractConditions
from ship import Ship
from grid import Grid
from game import Game
from player import Player
from fight import Fighting

if Game.start_game() == False:
    Game.start_game()
else:
    pass

dimention_game = Game.choosing()
Game.show_game_board(dimention_game)

player1 = Player(Game.name_players()[0], Grid(dimention_game).create_grid())
player2 = Player(Game.name_players()[1], Grid(dimention_game).create_grid())


def create_ships():
    global ship_start, ship_end
    ship_start, ship_end = [], []

    for player in [player1, player2]:
        print("_____________________")
        print("Hi "+player.name+" you can start creating your three ships")
        print("_____________________")
        for n in range(1,4):
            for i in range(0,2):
                if i == 0:
                    begining_ship_x =  InteractConditions(player.name, n).coordinate_conditions(dimention_game, "of the begining of yur ship "+str(n)+": ")
                    begining_ship_y = InteractConditions(player.name, n).coordinate_conditions(dimention_game, "of the begingin of yur ship "+str(n)+": ")
                else:
                    end_ship_x =  InteractConditions(player.name, n).coordinate_conditions(dimention_game, "of the end of yur ship "+str(n)+": ")
                    end_ship_x = InteractConditions(player.name, n).verticla_length(begining_ship_x, end_ship_x)
                    end_ship_y = InteractConditions(player.name, n).coordinate_conditions(dimention_game,  "of the end of yur ship "+str(n)+": ")
                    end_ship_y = InteractConditions(player.name, n).ship_conditions(begining_ship_x, begining_ship_y, end_ship_x, end_ship_y)
            ship_start.append(begining_ship_x)
            ship_start.append(begining_ship_y)
            ship_end.append(end_ship_x)
            ship_end.append(end_ship_y)

            Ship(player.grid, ship_start[0:2], ship_end[0:2]).creat_ship()
            ship_start, ship_end = [], []

create_ships()

Fighting(player1, player2, dimention_game).player_hit()
