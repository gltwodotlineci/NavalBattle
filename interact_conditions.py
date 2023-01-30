
class InteractConditions:
    def __init__(self, name_player, integer):
        self.name_player = name_player
        self.integer = integer
        self.add_value = 0

    def coordinate_conditions(self, dimention, phrase):
        coordinate_choice = int(input(self.name_player+" Choose the coordinate "+str(self.integer)+" "+phrase+" "))# of your missile attack: 
        if -1 < coordinate_choice and coordinate_choice < dimention:
            correct_coordinate = True
            return coordinate_choice
        else:
            correct_coordinate = False
            while correct_coordinate == False:
                coordinate_choice = int(input("Carefull the ccordinate must be between 0 and "+str(dimention-1)+" choose the coordinate " +str(self.integer)+" "+phrase+" "))#  of your missile attack: 
                if coordinate_choice >= 0 and coordinate_choice < dimention:
                    correct_coordinate = True
                else:
                    correct_coordinate = False

            return coordinate_choice


    def ship_conditions(self, x1, y1, x2, y2):
        match self.integer:    
            case 1:
                self.add_value = 2
                return self.ship_width(x1,y1,x2,y2)
            case 2:
                self.add_value = 4
                return self.ship_width(x1,y1,x2,y2)
            case 3:
                self.add_value = 6
                return self.ship_width(x1,y1,x2,y2)

    def ship_width(self, x1, y1, x2, y2):
        if x1 != x2:
            while y1 != y2:
                print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be "+str(y1))
                y2 = int(input("Give the second coorinate of your ship: "))
        else:
            if y2 != y1+ self.add_value:
                print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be " +str(y1+self.add_value)+ ". Because he width of Ship "+str(self.integer)+" must be "+str(self.add_value+1)+" units ")
                y2 = int(input("Give the second coorinate of the end of your ship: "))
            else:
                y2 = y2
        return y2


    def verticla_width(self,x1,x2):
        if x2 == x1:
            return x2
        else:
            if self.integer == 1:
                while x2 != x1 + 2:
                    print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be " +str(x1+2)+ ". Because he width of Ship "+str(self.integer)+" must be three units ")
                    x1 = int(input("Give the first coorinate of the begining of your ship: "))
            elif self.integer == 2:
                while x2 != x1 + 2:
                    print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be " +str(x1+2)+ ". Because he width of Ship "+str(self.integer)+" must be three units ")
                    x1 = int(input("Give the first coorinate of the begining of your ship: "))
            elif self.integer == 3:
                while x2 != x1 + 2:
                    print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be " +str(x1+2)+ ". Because he width of Ship "+str(self.integer)+" must be three units ")
                    x1 = int(input("Give the first coorinate of the begining of your ship: "))