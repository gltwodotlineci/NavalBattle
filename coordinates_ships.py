

class CoordinatesOfShips:
    def __init__(self, player_name):
        self.player_name = player_name
        self.coordinates_ships = {
            'ship_nb': [],
            'horizontal': [],
            'start_x': [],
            'start_y': [],
            'end_x': [],
            'end_y': []
        }


    def get_coordinates(self, ship_nb, start_x, start_y, end_x, end_y):
        self.coordinates_ships['ship_nb'].append(ship_nb)
        if start_x == end_x:
            self.coordinates_ships['horizontal'].append(1)
        else:
            self.coordinates_ships['horizontal'].append(0)
        self.coordinates_ships['start_x'].append(start_x)
        self.coordinates_ships['start_y'].append(start_y)
        self.coordinates_ships['end_x'].append(end_x)
        self.coordinates_ships['end_y'].append(end_y)

        return self.coordinates_ships