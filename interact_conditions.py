
class InteractConditions:

    def missile_conditions(name_player, dimention, integer):
        coordinate_choice = int(input(name_player+" Choose the coordinate "+str(integer)+" of your missile attack: "))
        if -1 < coordinate_choice and coordinate_choice < dimention:
            correct_coordinate = True
            return coordinate_choice
        else:
            correct_coordinate = False
            while correct_coordinate == False:
                coordinate_choice = int(input("Carefull the ccordinate must be between 0 and "+str(dimention-1)+" choose the coordinate " +str(integer)+ " of the missil: ")) 
                if coordinate_choice >= 0 and coordinate_choice < dimention:
                    correct_coordinate = True
                else:
                    correct_coordinate = False

            return coordinate_choice


    def ship_conditions():
        pass