from attack import Attack
from string import ascii_uppercase as letters


class Fighting:
    def __init__(self, gamer1, gamer2, dimention):
        self.gamer1 = gamer1
        self.gamer2 = gamer2
        self.dimention = dimention
        self.missile_coordinate = []
        self.succes = 1

 
    def show_ennemy_grid(self, var1, var2):
        for r in var1:
            for cel in r:
                if cel != "[o]":
                    var2.append(cel)
                elif cel == "[o]":
                    var2.append("(:)")

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


    def player_hit(self):
        prov = 0
        x_show, y_show = [], []
        while prov < 4:
            gamers = [self.gamer2, self.gamer1]
            for index, hit in enumerate(gamers):
                for j in range(1,3):
                    ele = int(input(hit.name+" Choose the coordinate "+str(j)+" of your missile attack "))
                    self.missile_coordinate.append(ele)
                if index == 0:
                    x = Attack(self.gamer1.grid, self.missile_coordinate, self.dimention).result_attack()
                    self.show_ennemy_grid(x, x_show)
                    x_show = []

                else:
                    y = Attack(self.gamer2.grid, self.missile_coordinate, self.dimention).result_attack()
                    self.show_ennemy_grid(y, y_show)
                    y_show = []
                self.missile_coordinate = []

            prov = prov + 1


    '''

    def check_win(self,contest1, contest2):
        self.succes = 0
        for r in contest1.grid:
            for cel in r:
                if cel == "[o]":
                    self.succes = self.succes + 1
        if self.succes == 0:
            while 1:
                if self.succes == 0:
                    print("*********************")
                    print(" ")
                    print("CONGRATS "+contest2.name+" YOU WON!!!")
                    print(" ")
                    print("*********************")
                    break

    '''
