from Enumerators import BidColor
from Controller import Controller
from Bid import Bid


class ComputerController(Controller):

    @staticmethod
    def bid(player, bidding, board):
        print("Now bids computer player:", player.position)
        max = bidding.highest_bid.number
        color = bidding.highest_bid.color
        my_color = None
        if color == BidColor.PASS:
            # first bidding of this player when no one bid before
            for i, count in enumerate(player.cards_amount):
                if count >= 5:
                    my_color = BidColor(i)
            if not my_color:
                return Bid(0, BidColor.PASS)
            else:
                return Bid(1, my_color)
        elif color == BidColor.N:
            # if a human player gives no color -> just pass
            return Bid(0, BidColor.PASS)
        else:
            eq_color = None
            # color you can raise when bidding number is equal
            co_player_known_cards = board.players[(player.position.value + 2) % 4].cards_known_amount

            for i in range(color.value + 1, 4):
                if player.cards_amount[i] + co_player_known_cards[i] == max+4:
                    print("My cards: ", player.cards_amount[i], " my co_player: ", co_player_known_cards[i])
                    eq_color = BidColor(i)
                elif player.cards_amount[i] + co_player_known_cards[i] > max+4:
                    # if on i-color we can gain more points
                    my_color = BidColor(i)
            if not my_color:
                if not eq_color:
                    if player.cards_amount[color.value] + co_player_known_cards[color.value] < max + 5:
                        return Bid(0, BidColor.PASS)
                    else:
                        return Bid(max+1, color)
                else:
                    return Bid(max, eq_color)
            else:
                return Bid(max+1, my_color)

    @staticmethod
    def play(player, game):
        card_to_beat = game.highest_in_four()
        highest_owner_position = game.highest_owner_position()
        color = game.current_color
        trump = game.trump

        if game.round_counter % 4 == 2:
            if highest_owner_position.on_same_team(player.position):
                if card_to_beat.figure.value < 11:
                    card = player.highest_card(card_to_beat, color, trump)
                else:
                    card = player.lowest_card(color, trump)
            else:
                card = player.highest_card(card_to_beat, color, trump)

        elif highest_owner_position.on_same_team(player.position):
            card = player.lowest_card(color, trump)
        else:
            card = player.higher_card(card_to_beat, color, trump)

        player.remove_card(card)

        return card

    @staticmethod
    def vist(player, game):
        lowest_card = None
        for cards in player.cards:
            for card in cards:
                if lowest_card is None:
                    lowest_card = card
                elif card < lowest_card:
                    lowest_card = card

        player.remove_card(lowest_card)

        return lowest_card



