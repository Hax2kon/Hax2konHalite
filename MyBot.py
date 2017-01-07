import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random


myID, game_map = hlt.get_init()
hlt.send_init("MyPythonBot")

# Create movement-function
def assign_move(square):
    if square.strength == 0:
        return Move(square, STILL)
    else:
        return Move(square, random.choice((NORTH, EAST, SOUTH, WEST, STILL)))

#Define moves-object, where moves will be stored
moves = []

# Game-structure:
while True:
    game_map.get_frame()

    for square in game_map:
        if square.owner == myID:
            moves.append(assign_move(square))

hlt.send_frame(moves)
