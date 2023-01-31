from string import ascii_uppercase as letters

class Game:

    def start_game():    
        global name, name2, choice

        print("Hi, welcom to Ship batle game, please choose your name and the dimention of the game!")
        name = input("What is you name player 1: ")
        dimention = input(" Welcome "+name+", you're the first player, the first player have the right to chose the dimention of the game \n what's the dimention of the game that you want to play? \n press 1 if you want a 8 x 8 dimention game \n press 2 if you want a  16 x 16 game\n press 3 if you want a  26 x 26 game\n ")
        choice = int(dimention)

        if choice == 1 or choice == 2 or choice == 3:
            correct = True
        else:
            correct = False

        while correct == False:
            input2 = input(" Wrong choice. you can only press 1, 2 or 3. \n press 1 if you want a 8 x 8 dimention game \n press 2 if you want a  16 x 16 game \n press 3 if you want a  26 x 26 game\n ")
            choice = int(input2)
            if choice == 1 or choice == 2 or choice == 3:
                correct = True


        print("Now the second player can write his hame and if he accept the dimention of the game proposed from the player")
        print('___________________________')
        name2 = input("Hello the player 2, what's your name? ")
        accept_dim = input("Welcome "+name2+", if you accept the dimention type 'Yes' ")
        if accept_dim != "Yes":
            print(" ")
            print("OK, You can start over from the begining than")
            print(" ___________________________")
            return False


    def choosing():
        match choice:
            case 1:
                return 8
            case 2:
                return 16
            case 3:
                return 26


    def name_players():
        return [name, name2]


    def show_game_board(dim):
        print(" ")
        print(" Hi this will be the Ship Batle game board!")
        print(" ")
        show_grid = [['(:)'] * dim for i in range(dim)]
        a_f = list(letters[:dim])
        num = iter(range(1,(dim+1)))
        print("     " + "   ".join(a_f))
        for row in show_grid:
            print(" ", next(num), end = " ")
            print(" ".join(row))
        print(" ")

    def player_game_board(name_player, grid, dim):
        print(" ")
        print(name_player+" this is your origin game board")
        a_f = list(letters[:dim])
        num = iter(range(1,(dim+1)))
        print("     " + "   ".join(a_f))
        for row in grid:
            print(" ", next(num), end = " ")
            print(" ".join(row))
        print(" ")
