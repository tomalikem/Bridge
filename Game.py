from Enumerators import *
from HumanController import HumanController


class Game:
    def __init__(self, players, play_maker_pos, trump):
        self.score_NS = 0
        self.score_EW = 0
        self.starting_position = PlayerPosition((play_maker_pos.value + 1) % 4)
        self.players = players
        self.trump = trump
        self.current_color = None
        self.four_cards = [None, None, None, None]
        self.round_counter = 0
    """Funkcja osbsługująca rozgrywkę, zwraca liczbę lew zebranych przez NS"""
    def game(self):
        while self.round_counter < 52:
            if self.round_counter % 4 == 0:
                for player in self.players:
                    if player.temporary_controller == HumanController:
                        player.print_cards()
                        print()
                if self.round_counter != 0:
                    self.score_four()

                pos = self.starting_position
                position = pos.value
                card = self.players[position].vist(self)

                self.four_cards[position] = card
                self.current_color = card.color
                card.print()
                print(" " + pos.str() + " vist")
            else:
                position = (self.round_counter + self.starting_position.value) % 4
                pos = PlayerPosition(position)
                card = self.players[position].play(self)
                self.four_cards[position] = card
                card.print()
                print(" " + pos.str())
            self.round_counter += 1
        return self.score_NS

    """Sprawdza czy wśród 4 dołożonych kart jest atut"""
    def trump_in_four(self):
        for card in self.four_cards:
            if card is not None and card.color == self.trump:
                return True
        return False

    """Zwraca najwyższą z kart w lewie"""
    def highest_in_four(self):
        max_card = None
        trump = self.trump_in_four()
        if trump:
            for card in self.four_cards:
                if card is not None and card.color == self.trump:
                    if max_card is None:
                        max_card = card
                    elif card > max_card:
                        max_card = card
        else:
            for card in self.four_cards:
                if card is not None and card.color == self.current_color:
                    if max_card is None:
                        max_card = card
                    if card > max_card:
                        max_card = card
        return max_card

    """Zwraca pozycję gracza, który dołożył najwyższą kartę w lewie, z uwzględnieniem atutów"""
    def highest_owner_position(self):
        max_card = self.highest_in_four()
        for i in range(4):
            card = self.four_cards[i]
            if card == max_card:
                return PlayerPosition(i)
        return None

    """Zlicza wyniki i czyści zmienne po dołożeniu 4tej karty"""
    def score_four(self):
        self.starting_position = self.highest_owner_position()
        self.four_cards = [None, None, None, None]

        if self.starting_position in [PlayerPosition.S, PlayerPosition.N]:
            self.score_NS = self.score_NS + 1
        else:
            self.score_EW = self.score_EW + 1
