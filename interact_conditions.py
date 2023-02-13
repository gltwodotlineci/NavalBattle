
class InteractConditions:
    def __init__(self, name_player, integer):
        self.name_player = name_player
        self.integer = integer
        self.add_value = 0


    def coordinate_conditions(self, dimention, coord_nb,phrase):
        '''
        The method make sure that the given coordinates of a ship or of
        a missile will not be outside the game border
        '''
        coordinate_choice_0 = (input(self.name_player+" Choose the coordinate "+str(coord_nb)+" "+phrase+" "))
        coordinate_choice = self.convert_char(coordinate_choice_0)
        if -1 < coordinate_choice and coordinate_choice < dimention:
            correct_coordinate = True
            return coordinate_choice
        else:
            correct_coordinate = False
            while correct_coordinate == False:
                coordinate_choice_0 = (input("Carefull the ccordinate must be between A and "+chr(dimention+64)+" choose the coordinate " +str(self.integer)+" "+phrase+" "))#  of your missile attack: 
                coordinate_choice = self.convert_char(coordinate_choice_0)
                if coordinate_choice >= 0 and coordinate_choice < dimention:
                    correct_coordinate = True
                else:
                    correct_coordinate = False

            return coordinate_choice


    def ship_conditions(self, x1, y1, x2, y2):
        self.add_value = 6
        if self.integer == 1:
            self.add_value = 2
        elif self.integer == 2:
            self.add_value == 4
        return self.ship_width(x1,y1,x2,y2)



    def ship_width(self, x1, y1, x2, y2):
        '''
        The mathod will garentie that the ship will not be biger or smaller
        than the game conditions.
        Example, if the first ship must be 3 units large and the player will
        make a ship of 2 or 4 units large, the method will stop it and sugest
        to the player the right size
        '''
        if x1 != x2:
            while y1 != y2:
                print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be "+(chr(y1+65)))
                y2_0= (input("Give the second coorinate of your ship: "))
                y2 = self.convert_char(y2_0)
        else:
            while y2 != y1+ self.add_value:
                print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be " +chr(y1+self.add_value+65)+ ". Because he width of Ship "+str(self.integer)+" must be "+str(self.add_value+1)+" units ")
                y2_0 = (input("Give the second coorinate of the end of your ship: "))
                y2 = self.convert_char(y2_0)
        return y2


    def verticla_length(self,x1,x2):
        '''
        The same thing like in the 'ship_width' method, but thise time for
        the vertical case
        '''
        if x2 == x1:
            return x2
        else:
            if self.integer == 1:
                while x2 != x1 + 2:
                    print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be " +chr(x1+2+65)+ ". Because the vertical length of Ship "+str(self.integer)+" must be three units ")
                    x2_0 = (input("Give the first coorinate of the end of your ship: "))
                    x2 = self.convert_char(x2_0)
            elif self.integer == 2:
                while x2 != x1 + 4:
                    print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be " +chr(x1+4+65)+ ". Because the vertical length of Ship "+str(self.integer)+" must be five units ")
                    x2_0 = (input("Give the first coorinate of the end of your ship: "))
                    x2 = self.convert_char(x2_0)
            elif self.integer == 3:
                while x2 != x1 + 6:
                    print("Erreur! Attention "+self.name_player+ " it is possible that your coordinate might be " +chr(x1+6+65)+ ". Because the vertical length of Ship "+str(self.integer)+" must be sseven units ")
                    x2_0 = (input("Give the first coorinate of the end of your ship: "))
                    x2 = self.convert_char(x2_0)
            return x2


    def convert_char(self, char):
        return ord(char) - 65
