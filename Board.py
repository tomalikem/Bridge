from Player import Player
from Bidding import Bidding
from Game import Game
from Enumerators import CardColor, CardFigure, PlayerPosition
import itertools, random
from Card import Card


class Board:
    def __init__(self, starting_bidder, s, w, n, e):
        self.contract_color = None
        self.contract_height = None
        self.result = None
        self.starting_bidder = starting_bidder
        self.play_maker = None
        self.players = [s, w, n, e]

    def deal_cards(self):
        deck = list(itertools.product(list(CardFigure), list(CardColor)))
        random.shuffle(deck)

        for i in range(52):
            self.players[i % 4].cards[deck[i][1].value].append(Card(deck[i][1], deck[i][0]))

        for player in self.players:
            player.count_points()
            player.count_cards()

    def set_contract(self):
        bidding = Bidding(self.starting_bidder)
        bidding.bidding(self)
        self.play_maker = bidding.highest_bidder
        (self.contract_height, self.contract_color) = (bidding.highest_bid.number, bidding.highest_bid.color)
        """Starting player position missing"""

    def play_game(self):
        """S is Human, W, N, E are computers"""
        if self.play_maker is not None:
            co_player_pos = PlayerPosition.co_player(self.play_maker.position)
            co_player = self.players[co_player_pos.value]
            co_player.give_control_to(self.play_maker)

            game = Game(self.players, self.play_maker.position, self.contract_color)
            self.result = game.game()

            co_player.retake_control()





