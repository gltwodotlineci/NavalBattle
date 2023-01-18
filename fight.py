from attack import Attack

class Fighting:
    def __init__(self, gamer1, gamer2, dimention):
        self.gamer1 = gamer1
        self.gamer2 = gamer2
        self.dimention = dimention
        self.missile_coordinate = []
        self.succes = 1

    def check_win(self,contest1, contest2):
        Attack(contest1.grid, self.missile_coordinate, self.dimention).result_attack()
        self.succes = 0
        self.missile_coordinate = []
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

    def fighting(self):
        print("The gamer One had the advantage of choosing the game dimention.\n So, the gamer 2 will star the attack")
        while self.succes > 0:
            for index, gamer in enumerate([self.gamer2, self.gamer1]):
                for j in range(1,3):
                    ele = int(input(gamer.name+" Choose the coordinate "+str(j)+" of your missile attack "))
                    self.missile_coordinate.append(ele)
                if index == 0:
                    self.check_win(self.gamer1, self.gamer2)
                else:
                    self.check_win(self.gamer2, self.gamer1)
