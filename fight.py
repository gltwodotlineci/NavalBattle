from attack import Attack
from string import ascii_uppercase as letters


class Fighting:
    def __init__(self, gamer1, gamer2, dimention):
        self.gamer1 = gamer1
        self.gamer2 = gamer2
        self.dimention = dimention
        self.missile_coordinate = []
        self.succes = False

 
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

        mat = []
        while var2 != []:
            mat.append(var2[:self.dimention])
            var2 = var2[self.dimention:]
        a_f = list(letters[:self.dimention])
        num = iter(range(1,(self.dimention+1)))
        print("     " + "   ".join(a_f))
        for row in mat:
            print(" ", next(num), end = " ")
            print(" ".join(row))


    def check_win(self, player):
        if self.succes == True:
            print(" ")
            print("*********************")
            print(" ")
            print("CONGRATS "+player+" YOU WON!!!")
            print(" ")
            print("*********************")


    def player_hit(self):
        x_show, y_show = [], []
        while self.succes != True:
            gamers = [self.gamer2, self.gamer1]
            for index, hit in enumerate(gamers):
                for j in range(1,3):
                    ele = int(input(hit.name+" Choose the coordinate "+str(j)+" of your missile attack "))
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

