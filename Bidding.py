from Enumerators import *
from Bid import Bid
from Player import Player


class Bidding:
    def __init__(self, player):
        self.highest_bid = Bid(0, BidColor.PASS)
        self.starting_player = player
        self.counter = 0
        self.pass_counter = 0
        self.highest_bidder = None

        '''Słowniki zawierające kolor jako klucz i player_position jako wartość'''
        self.NS_contractor = [None, None, None, None, None]
        self.EW_contractor = [None, None, None, None, None]

    def bidding(self, board):
        """TO DO - zwraca highest bid i ustawia rozgrywającego w boardzie"""
        current_player = self.starting_player
        self.highest_bidder = None
        min_to_start = 12
        while min_to_start > 0:
            if current_player.points < min_to_start:
                current_player = board.players[(current_player.position.value + 1) % 4]
                self.pass_counter += 1
            else:
                self.pass_counter = 0
                break
            if self.pass_counter == 4:
                min_to_start -= 1
                self.pass_counter = 0

        while self.pass_counter != 4:
            bidding = current_player.bid(self, board)
            if bidding == Bid(0, BidColor.PASS):
                print("Player PASSED")
                self.pass_counter += 1
            else:
                self.highest_bidder = current_player
                self.highest_bid = bidding
                self.pass_counter = 0
                friend_player = board.players[(self.highest_bidder.position.value + 2) % 4]
                if bidding.color != BidColor.N:
                    if friend_player.cards_known_amount[bidding.color.value] > 0 \
                            and friend_player.last_bid.color == bidding.color:
                        friend_player.cards_known_amount[bidding.color.value] = bidding.number - friend_player.last_bid.number
                    else:
                        board.players[self.highest_bidder.position.value].cards_known_amount[bidding.color.value] = bidding.number + 4
                current_player.last_bid = bidding
                if self.highest_bidder.position == PlayerPosition.S or self.highest_bidder.position == PlayerPosition.N:
                    current_contractor = self.NS_contractor
                else:
                    current_contractor = self.EW_contractor
                if not current_contractor[bidding.color.value]:
                    current_contractor[bidding.color.value] = self.highest_bidder
            current_player = board.players[(current_player.position.value + 1) % 4]
            print("Highest bid is now: ", self.highest_bid)
        if self.highest_bidder is None:
            return None, None
        if self.highest_bidder.position == PlayerPosition.S or self.highest_bidder.position == PlayerPosition.N:
            current_contractor = self.NS_contractor
        else:
            current_contractor = self.EW_contractor
        return self.highest_bid, current_contractor[self.highest_bid.color.value]




