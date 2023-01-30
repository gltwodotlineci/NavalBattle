from attack import Attack
from string import ascii_uppercase as letters
from interact_conditions import InteractConditions


class Fighting:
    def __init__(self, gamer1, gamer2, dimention):
        self.gamer1 = gamer1
        self.gamer2 = gamer2
        self.dimention = dimention
        self.missile_coordinate = []
        self.succes = False

    def recreate_grid(self,new_grid):
        mat = []
        while new_grid != []:
            mat.append(new_grid[:self.dimention])
            new_grid = new_grid[self.dimention:]
        a_f = list(letters[:self.dimention])
        num = iter(range(1,(self.dimention+1)))
        print("Your ennemy gamefield!")
        print("     " + "   ".join(a_f))
        for row in mat:
            print(" ", next(num), end = " ")
            print(" ".join(row))


    def show_ennemy_grid(self, var1, var2):
        count = 0
        for r in var1:
            for cel in r:
                if cel != "[o]":
                    var2.append(cel)
                elif cel == "[o]":
                    var2.append("(:)")
                    count = count + 1 # Will be used to check win

        if count == 0:
            self.succes = True

        self.recreate_grid(var2)

    def show_your_own_grid(self, player, grid):
        print(" ---____----___---")
        print("Hi "+player+" Do you want to see your own game field?")
        print(" write 'yes' if you want to see your game field and 'no' if not ")
        answer = input("yes/no ")
        if answer == "yes":
            a_f = list(letters[:self.dimention])
            num = iter(range(1,(self.dimention+1)))
            print( " YOUR OWN GAMEFIELD")
            print("     " + "   ".join(a_f))
            for row in grid:
                print(" ", next(num), end = " ")
                print(" ".join(row))
            print("    ")
        else:
            pass



    def check_win(self, player):
        if self.succes == True:
            print(" ")
            print("*********************")
            print(" ")
            print("CONGRATS "+player+" YOU WON!!!")
            print(" ")
            print("*********************")


    def player_hit(self):
        count = 0
        x_show, y_show = [], []
        while self.succes != True:
            gamers = [self.gamer2, self.gamer1]
            for index, hit in enumerate(gamers):
                if count > 0:
                    if index == 0:
                        self.show_your_own_grid(self.gamer2.name,y)
                    else:
                        self.show_your_own_grid(self.gamer1.name,x)
                for j in range(1,3):
                    ele = InteractConditions(hit.name, j).coordinate_conditions(self.dimention, "of your missile attack:")
                    self.missile_coordinate.append(ele)
                if index == 0:
                    x = Attack(self.gamer1.grid, self.missile_coordinate).result_attack()
                    self.show_ennemy_grid(x, x_show)
                    x_show = []

                    self.check_win(self.gamer2.name)
                    if self.succes == True:
                        break

                else:
                    y = Attack(self.gamer2.grid, self.missile_coordinate).result_attack()
                    self.show_ennemy_grid(y, y_show)
                    y_show = []

                    self.check_win(self.gamer1.name)
                    if self.succes == True:
                        break

                self.missile_coordinate = []
            count = count + 1
