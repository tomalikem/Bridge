from ComputerController import ComputerPlayer
from HumanController import HumanPlayer


class Conversion:

    @staticmethod
    def convert_to_computer(player):
        computer_player = ComputerPlayer(player.position)
        computer_player.cards = player.cards
        computer_player.known_cards = player.known_cards
        computer_player.cards_known_amount = player.cards_known_amount
        computer_player.points = player.points
        computer_player.last_bid = player.last_bid
        computer_player.known_points = player.known_points
        computer_player.position = player.position
        computer_player.cards_amount = player.cards_amount

        return computer_player

    @staticmethod
    def convert_to_human(player):
        human_player = HumanPlayer(player.position)
        human_player.cards = player.cards
        human_player.known_cards = player.known_cards
        human_player.cards_known_amount = player.cards_known_amount
        human_player.points = player.points
        human_player.last_bid = player.last_bid
        human_player.known_points = player.known_points
        human_player.position = player.position
        human_player.cards_amount = player.cards_amount

        return human_player
