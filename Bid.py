from Enumerators import *


class Bid:
    def __init__(self, number, color):
        self.color = color
        self.number = number

    def __eq__(self, other):
        if self is None or other is None:
            return False
        if self.color == other.color and self.number == other.number:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.number > other.number:
            return True
        elif self.number == other.number:
            if self.color.value > self.color.value:
                return True
        else:
            return False

    def __lt__(self, other):
        if self.number < other.number:
            return True
        elif self.number == other.number:
            if self.color.value < other.color.value:
                return True
        else:
            return False

    def __str__(self):
        if self.color == BidColor.PASS or not self.number or not self.color:
            return "PASS"
        return str(self.number) + self.color.str()


    @staticmethod
    def string_to_bid(string):
        if len(string) == 2:
            fig_str = string[0]
            col_str = string[1]
        elif len(string) == 3:
            fig_str = string[0:2]
            col_str = string[2]
        else:
            return None

        if col_str == "S":
            color = BidColor.S
        elif col_str == "H":
            color = BidColor.H
        elif col_str == "D":
            color = BidColor.D
        elif col_str == "C":
            color = BidColor.C
        elif col_str == "N":
            color = BidColor.N
        else:
            color = None

        figure = (int(fig_str))

        return Bid(figure, color)
