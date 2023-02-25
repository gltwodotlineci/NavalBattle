# The Battleship game (Naval Batle)

##### The game will be alsow published in 'https://github.com/GlenDrs'

Battleship is game played between two players. Originaly a french game named otherwise Bataille Navale.
the previews adresse will tell you more about the rules of the game: https://www.cs.nmsu.edu/~bdu/TA/487/brules.htm

At this stage the game will be played in one terminal and it is developed in a way that once a player have finished his attack or watching his game field he can hide it before the adverse take the screen.

The choice was made that the game might have Three types of board games. A 8x8 dimension, a 16x16 dimension and a 26x26 dimension. The first player chose the dimension and the second player will accept or not the board game dimension. The first which will attack will be the second player.

The coordinates for the ship or the missile will be alphabetically. A to H for 8x8, A to P for the 16x16 game dimension and A to Z for the last one.

### Here is a empty board game example:

     A   B   C   D   E   F   G   H
  A  (:)  (:)  (:)  (:)  (:)  (:)  (:)  (:)\
  B  (:)  (:)  (:)  (:)  (:)  (:)  (:)  (:)\
  C  (:)  (:)  (:)  (:)  (:)  (:)  (:)  (:)\
  D  (:)  (:)  (:)  (:)  (:)  (:)  (:)  (:)\
  E  (:)  (:)  (:)  (:)  (:)  (:)  (:)  (:)\
  F  (:)  (:)  (:)  (:)  (:)  (:)  (:)  (:)\
  G  (:)  (:)  (:)  (:)  (:)  (:)  (:)  (:)\
  H  (:)  (:)  (:)  (:)  (:)  (:)  (:)  (:)

  Example 1*8x8 dimesion game*.

_**the symbols are: (:) for empty space**_.

        [o] the simbol of a part of the ship.
        [#] when the missile has hit the target.
        -No when the missile has missed the target.

### Here is a game situation.

     A   B   C   D   E   F   G   H
  A  [o]  [o]  [#]  (:)  (:)  (:)  (:)  [o]\
  B  (:)  (:)  (:)  (:)  (:)  (:)  (:)  [o]\
  C  (:)  (:)  (:)  -No  (:)  (:)  (:)  [o]\
  D  (:)  (:)  (:)  (:)  (:)  (:)  (:)  [o]\
  E  (:)  (:)  (:)  (:)  (:)  (:)  (:)  [o]\
  F  (:)  (:)  (:)  (:)  (:)  (:)  (:)  (:)\
  G  (:)  (:)  (:)  (:)  (:)  (:)  (:)  (:)\
  H  [o]  [o]  [o]  [o]  [o]  [o]  [o]  (:)

  Example 2 *8x8 dimesion game*.


_**In this game the ship is hited once in the coordinate (A:C) and missed once in the coordinate (C:D)**_.

At this moment the choice for the ships is that we'll have 3 ships. The first one will be three units, the second one 5 and the third 7.

--------------------------------------------------------------------

In this game you can't start placing the ship in a decreasing way (Vertically or horizontally) for example, the ship between (A:A) and (A:C). When you give the coordinates to place the ship in this way you can't give the coordinates (A:C) for the beginning of the ship and (A:A) for the end of the ship. You must give the (A:A) for the beginning and (A:C) for the end. the same for the ship between (A:H) to (E:H), you can't start in (E:H) and end in (A:H).

###* Some advantages of the game are that, the game will not let you lance a missile outside the game field and also it will not permit you to build a ship bigger or smaller of the appropriated ship.  The game also will check the coordinates of the beginning of your ship and if the end of the ship is not possible because of the coordinates of the beginning of the ship it will ask you to start over. If in the *example 2* the coordinates of the third ship (7 units) will be in (E:H) it is clear that the end will be outside the game field. So the game will ask you again the coordinates for the ship 3.

###* The board gama advantages. The game will be played in the same screen. So in order to prevent the enemy to see other's position the game will clean the sreen before the player switch game. At the same time each player in his screen can see his own game field.His ships, missels that missed him and missels that touched his ships. He can check the same for his enamy game field exept the enemy's ships.

###* Also if some part (or all) of your ship will be placed on top of an existing ship the game will ask you to start over. In the example 2 we have the second ship placed in (A:H) - (E:H), so if your third ship will touch one of the cells between (A:H) and (E:H), the game will ask you to start from the beginging the placment of the ship 3.
