from Player import Player
from Enumerators import BidColor
from Card import Card
from Controller import Controller
from Bid import Bid


class HumanController(Controller):

    @staticmethod
    def bid(player, bidding, board):
        print("Now bids human player: ", player.position)
        HumanController.showCards(player)
        print("Input: number color")
        try:
            bid_string = str(input()).strip().upper()
            if bid_string == "0":
                return Bid(0, BidColor.PASS)
            bid = Bid.string_to_bid(bid_string)
            if not bid:
                print("There is no such color, input again")
                return HumanController.bid(player, bidding, board)
        except KeyboardInterrupt:
            print("That was not a number. Please insert again.")
            return HumanController.bid(player, bidding, board)
        except ValueError:
            print("That was not a number. Please insert again.")
            return HumanController.bid(player, bidding, board)
        if bid == bidding.highest_bid:
            print("This bidding is equal last highest bid: ", bidding, " you have to bid again")
            return HumanController.bid(player, bidding, board)
        if bid < bidding.highest_bid:
            print("This bidding is lower than last highest bid: ", bidding, " you have to bid again")
            return HumanController.bid(player, bidding, board)

        return bid


    @staticmethod
    def play(player, game):
        print("Turn of player", player.position)
        HumanController.showCards(player)
        print("Chose card")
        card_string = str(input()).strip()
        card = Card.string_to_card(card_string)
        if player.have(card) and player.can_play(card, game.current_color):
            player.remove_card(card)
        else:
            if not player.have(card):
                print("You dont have that card")
            else:
                print("You have to play card of color: ", game.current_color)
            player.play(game)
        return card

    @staticmethod
    def vist(player, game):
        print("Vist of player", player.position)
        HumanController.showCards(player)
        print("Chose card")
        card_string = str(input()).strip()
        card = Card.string_to_card(card_string)
        if player.have(card):
            player.remove_card(card)
        else:
            print("You dont have that card")
            player.vist(game)
        return card


    @staticmethod
    def showCards(player):
        for i in player.cards:
            for card in i:
                print(card, end=" ")
            print(""),


