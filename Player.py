from Enumerators import *
import abc

class Player:
    def __init__(self, position, controller):
        self.cards = [[], [], [], [], []]
        self.known_cards = [[], [], [], [], []]
        self.cards_known_amount = [0, 0, 0, 0, 0]
        self.points = 0
        self.last_bid = (0, BidColor.PASS)
        self.known_points = 0
        self.position = position
        self.cards_amount = [0, 0, 0, 0, 0]
        self.main_controller = controller
        self.temporary_controller = controller

    def bid(self, bidding, board):
        return self.temporary_controller.bid(self, bidding, board)

    def play(self, game):
        return self.temporary_controller.play(self, game)

    def vist(self, game):
        return self.temporary_controller.vist(self, game)

    def count_cards(self):
        for i, card_color in enumerate(self.cards):
            for card in card_color:
                self.cards_amount[i] += 1

    def count_all_cards(self):
        counter = 0
        for i, card_color in enumerate(self.cards):
            for card in card_color:
                counter += 1
        print(counter, end=" ")

    def count_points(self):
        x = 0
        for card_color in self.cards:
            for card in card_color:
                if card.figure.value > 10:
                    x += card.figure.value - 10
        self.points = x

    def have(self, card1):
        for cards in self.cards:
            for card2 in cards:
                if card1 == card2:
                    return True
        return False

    def can_play(self, card, current_color):
        if card.color == current_color:
            return True
        elif len(self.cards[current_color.value]) == 0:
            return True
        else:
            return False

    def remove_card(self, card_to_remove):
        cards = self.cards[card_to_remove.color.value]
        cards.remove(card_to_remove)

    def lowest_card(self, color, trump):
        lowest_card = None
        if len(self.cards[color.value]) > 0:
            for card in self.cards[color.value]:
                if lowest_card is None:
                    lowest_card = card
                elif lowest_card > card:
                    lowest_card = card
        else:
            for cards in self.cards:
                for card in cards:
                    if lowest_card is None or (lowest_card.color == trump and card.color == trump):
                        if lowest_card is None:
                            lowest_card = card
                        elif lowest_card > card:
                            lowest_card = card
                    elif lowest_card.color == trump:
                        lowest_card = card
                    elif lowest_card > card:
                        lowest_card = card
        return lowest_card

    def highest_card(self, card_to_beat, color, trump):
        if len(self.cards[color.value]) > 0:
            highest_card = self.highest_in_color(color)
            if highest_card.color == card_to_beat.color and highest_card < card_to_beat:
                highest_card = self.lowest_card(color, trump)
        else:
            highest_card = self.lowest_card(trump, trump)
        return highest_card

    def highest_in_color(self,  color):
        highest_card = None
        for cards in self.cards:
            for card in cards:
                if card.color == color:
                    if highest_card is None:
                        highest_card = card
                    elif highest_card < card:
                        highest_card = card
        return highest_card

    def higher_in_color(self, card_to_beat):
        higher_card = None
        for cards in self.cards:
            for card in cards:
                if card.color == card_to_beat.color:
                    if higher_card is None:
                        higher_card = card
                    elif higher_card > card > card_to_beat:
                        higher_card = card
                    elif card_to_beat > higher_card > card:
                        higher_card = card
        return higher_card

    def higher_card(self, card_to_beat, color, trump):
        if card_to_beat.color == color:
            if len(self.cards[color.value]) > 0:
                return self.higher_in_color(card_to_beat)
            else:
                return self.lowest_card(trump, trump)
        else:
            if len(self.cards[color.value]) > 0:
                return self.lowest_card(color, trump)
            else:
                return self.lowest_card(trump, trump)

    def print_cards(self):
        print(self.position)
        for cards in self.cards:
            for card in cards:
                card.print()
            print()

    def give_control_to(self, player):
        self.temporary_controller = player.main_controller

    def retake_control(self):
        self.temporary_controller = self.main_controller









