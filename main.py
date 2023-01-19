from ship import Ship
from grid import Grid
from game import Game
from player import Player
from fight import Fighting

Game.start_game()

dimention_game = Game.choosing()
player1 = Player(Game.name_players()[0], Grid(dimention_game).create_grid())
player2 = Player(Game.name_players()[1], Grid(dimention_game).create_grid())


def create_ships():
    global ship_start, ship_end
    ship_start, ship_end = [], []

    for player in [player1, player2]:
        print("_____________________")
        print("Hi "+player.name+" you can start creating your three ships")
        print("_____________________")
        for n in range(1,2):
            for i in range(0,2):
                if i == 0:
                    ship_start.append(int(input("Choose the 1st coordinate for the start of ship "+str(n)+" ")))
                    ship_start.append(int(input("Choose the second coordinate for the start of ship "+str(n)+" ")))
                elif i == 1:
                    ship_end.append(int(input("Choose the 1st coordinate for the end of ship "+str(n)+" ")))
                    ship_end.append(int(input("Choose the second coordinate for the end of ship "+str(n)+" ")))

            Ship(player.grid, ship_start[0:2], ship_end[0:2]).creat_ship()
            ship_start, ship_end = [], []

create_ships()

Fighting(player1, player2, dimention_game).fighting()