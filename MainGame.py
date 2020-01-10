from Board import Board
from Game import *
from HumanController import *
from ComputerController import *
import os


def start_game():
    starting_player = PlayerPosition.S
    # s = Player(PlayerPosition.S, ComputerController)
    # w = Player(PlayerPosition.W, ComputerController)
    # n = Player(PlayerPosition.N, ComputerController)
    # e = Player(PlayerPosition.E, ComputerController)
    s = Player(PlayerPosition.S, HumanController)
    w = Player(PlayerPosition.W, ComputerController)
    n = Player(PlayerPosition.N, ComputerController)
    e = Player(PlayerPosition.E, ComputerController)
    board = Board(s, s, w, n, e)

    board.deal_cards()
    board.set_contract()
    if board.contract_color == BidColor.PASS:
        print("\nCONTRACT COULDN'T BE SET.\n")
        exit(0)
    board.play_game()

if __name__== "__main__":
    for i in range(1):
        start_game()

