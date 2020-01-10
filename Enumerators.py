from enum import Enum


class PlayerPosition(Enum):
    S = 0
    W = 1
    N = 2
    E = 3

    def str(self):
        if self == PlayerPosition.S:
            return "S"
        elif self == PlayerPosition.W:
            return "W"
        elif self == PlayerPosition.N:
            return "N"
        else:
            return "E"

    def on_same_team(self, other):
        if(self.value - other.value) % 2 == 0:
            return True
        else:
            return False

    def co_player(self):
        return PlayerPosition((self.value + 2) % 4)






"""Clubs, Diamonds, Hearts, Spades"""


class CardColor(Enum):
    C = 0
    D = 1
    H = 2
    S = 3

    def str(self):
        if self == CardColor.S:
            return "\u2664"
        elif self == CardColor.H:
            return "\u2661"
        elif self == CardColor.D:
            return "\u2662"
        else:
            return "\u2667"


class CardFigure(Enum):
    Ace = 14
    King = 13
    Queen = 12
    Jack = 11
    Ten = 10
    Nine = 9
    Eight = 8
    Seven = 7
    Six = 6
    Five = 5
    Four = 4
    Three = 3
    Two = 2

    def str(self):
        if self == CardFigure.Ace:
            return "A"
        elif self == CardFigure.King:
            return "K"
        elif self == CardFigure.Queen:
            return "Q"
        elif self == CardFigure.Jack:
            return "J"
        else:
            return str(self.value)


"""Clubs, Diamonds, Hearts, Spades, None, PASS, COUNTER, RE COUNTER"""


class BidColor(Enum):
    C = 0
    D = 1
    H = 2
    S = 3
    N = 4
    PASS = 5
    CR = 6
    RCR = 7

    def str(self):
        if self == BidColor.S:
            return "\u2664"
        elif self == BidColor.H:
            return "\u2661"
        elif self == BidColor.D:
            return "\u2662"
        elif self == BidColor.C:
            return "\u2667"
        elif self == BidColor.N:
            return "NoColor"
        elif self == BidColor.PASS:
            return "PASS"
        elif self == BidColor.C:
            return "Counter"
        else:
            return "ReCounter"



def bid_to_card_color(bid_color):
    if bid_color.value < 4:
        return CardColor(bid_color.value)
    else:
        return None


class Team(Enum):
    CoPlayer = 0
    Opponent = 1
