from Player import Player
from Bidding import Bidding
from Game import Game
from Enumerators import CardColor, CardFigure, PlayerPosition
import itertools, random
from Card import Card
from HumanController import HumanController
from ComputerController import ComputerController


class GameTestingBoard:
    def __init__(self):
        s = Player(PlayerPosition.S, HumanController)
        w = Player(PlayerPosition.W, ComputerController)
        n = Player(PlayerPosition.N, ComputerController)
        e = Player(PlayerPosition.E, ComputerController)
        self.contract_color = CardColor.S
        self.contract_height = 4
        self.result = None
        self.players = [s, w, n, e]
        self.play_maker = s
        self.deal_cards()
        self.play_game()

    def deal_cards(self):
        deck = list(itertools.product(list(CardFigure), list(CardColor)))
        random.shuffle(deck)

        for i in range(52):
            self.players[i % 4].cards[deck[i][1].value].append(Card(deck[i][1], deck[i][0]))

        for player in self.players:
            player.count_points()
            player.count_cards()

    def play_game(self):
        """S is Human, W, N, E are computers"""
        co_player_pos = PlayerPosition.co_player(self.play_maker.position)
        co_player = self.players[co_player_pos.value]
        co_player.give_control_to(self.play_maker)

        game = Game(self.players, self.play_maker.position, self.contract_color)
        self.result = game.game()

        co_player.retake_control()


for i in range(1):
    game = GameTestingBoard()
    print(game.result)
