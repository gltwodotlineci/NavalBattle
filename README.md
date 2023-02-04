# The Battleship game (Naval Batle)

Battleship is game played between two players. Originaly a french game named otherwise Bataille Navale.
the previews adresse will tell you more about the rules of the game: https://www.cs.nmsu.edu/~bdu/TA/487/brules.htm

At this stage the game will be played in one terminal and it is developed in a way that once a player have finished his attack or watching his game field he can hide it before the adverse take the screen.

The choice was made that the game might have Three types of board games. A 8x8 dimension, a 16x16 dimension and a 26x26 dimension. The first player chose the dimension and the second player will accept or not the board game dimension. The first which will attack will be the second player.

The coordinates for the ship or the missile will be alphabetically. A to H for 8x8, A to P for the 16x16 game dimension and A to Z for the last one.

### Here is a empty board game example:

     A   B   C   D   E   F   G   H
  A (:) (:) (:) (:) (:) (:) (:) (:)

  B (:) (:) (:) (:) (:) (:) (:) (:)

  C (:) (:) (:) (:) (:) (:) (:) (:)

  D (:) (:) (:) (:) (:) (:) (:) (:)

  E (:) (:) (:) (:) (:) (:) (:) (:)

  F (:) (:) (:) (:) (:) (:) (:) (:)

  G (:) (:) (:) (:) (:) (:) (:) (:)

  H (:) (:) (:) (:) (:) (:) (:) (:)

  *8x8 dimesion game

***the symbols are: (:) for empty space
                    [o] the simbol of a part of the ship.
                    [#] when the missile has hit the target.
                    -No when the missile has missed the target.

### Here is a game situation.

     A   B   C   D   E   F   G   H
  A [o] [o] [#] (:) (:) (:) (:) [o]\
  B (:) (:) (:) (:) (:) (:) (:) [o]\
  C (:) (:) (:) -No (:) (:) (:) [o]\
  D (:) (:) (:) (:) (:) (:) (:) [o]\
  E (:) (:) (:) (:) (:) (:) (:) [o]\
  F (:) (:) (:) (:) (:) (:) (:) (:)\
  G (:) (:) (:) (:) (:) (:) (:) (:)\
  H [o] [o] [o] [o] [o] [o] [o] (:)

*In this game the ship is hited once in the coordinate (A:C) and missed once in the coordinate (C:D)

At this moment the choice for the ships is that we'll have 3 ships. The first one will be three units, the second one 5 and the third 7.

--------------------------------------------------------------------

In this game you can't start placing the ship in a decreasing way (Vertically or horizontally) for example, the ship between (A:A) and (A:C). When you give the coordinates to place the ship in this way you can't give the coordinates (A:C) for the beginning of the ship and (A:A) for the end of the ship. You must give the (A:A) for the beginning and (A:C) for the end. the same for the ship between (A:H) to (E:H), you can't start in (E:H) and end in (A:H).

###* Some advantages of the game are that, the game will not let you lance a missile outside the game field and also it will not permit you to build a ship bigger or smaller of the appropriated ship.