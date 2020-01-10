from Enumerators import *


class Card:
    def __init__(self, color, figure):
        self.color = color
        self.figure = figure

    def __eq__(self, other):
        if self is None or other is None:
            return False
        if self.color == other.color and self.figure == other.figure:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.figure.value > other.figure.value:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.figure.value < other.figure.value:
            return True
        else:
            return False

    def __str__(self):
        return self.figure.str() + self.color.str()

    def print(self):
        print(self.figure.str() + self.color.str(), end=" ")


    @staticmethod
    def string_to_card(string):
        if len(string) == 2:
            fig_str = string[0]
            col_str = string[1]
        elif len(string) == 3:
            fig_str = string[0:2]
            col_str = string[2]
        else:
            return None

        if col_str == "S":
            color = CardColor.S
        elif col_str == "H":
            color = CardColor.H
        elif col_str == "D":
            color = CardColor.D
        elif col_str == "C":
            color = CardColor.C
        else:
            color = None

        if fig_str == "A":
            figure = CardFigure(14)
        elif fig_str == "K":
            figure = CardFigure(13)
        elif fig_str == "Q":
            figure = CardFigure(12)
        elif fig_str == "J":
            figure = CardFigure(11)
        else:
            figure = CardFigure(int(fig_str))

        return Card(color, figure)


