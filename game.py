
class Game:

    def start_game():    
        global name, name2, choice

        print("Hi, welcom to Ship batle game, please choose your name and the dimention of the game!")
        name = input("What is you name player 1: ")
        dimention = input(" Welcome "+name+", you're the first player, the first player have the right to chose the dimention of the game \n what's the dimention of the game that you want to play? \n press 1 if you want a 8 x 8 dimention game \n press 2 if you want a  16 x 16 game\n press 3 if you want a  26 x 26 game\n ")
        choice = int(dimention)

        while choice > 3:
            input2 = input(" Wrong choice. you can only press 1, 2 or 3. \n press 1 if you want a 8 x 8 dimention game \n press 2 if you want a  16 x 16 game \n press 3 if you want a  26 x 26 game\n ")
            choice = int(input2)

        print("Now the second player can write his hame and if he accept the dimention of the game proposed from the player")
        print('___________________________')
        name2 = input("Hello the player 2, what's your name? ")
        accept_dim = input("Welcome "+name2+", if you accept the dimention type 'Yes' ")
        if accept_dim != "Yes":
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
