import random


class Deck():

    def __init__(self):
        pass

    rank = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    # clubs (♣), diamonds (♦), hearts (♥) and spades (♠)
    suits = ('clubs', 'diamonds', 'hearts', 'spades')
    suits_icons = ('♣', '♦', '♥', '♠')

    def get_card(self):
        # this method returns a tuple
        return random.choice(self.rank), random.choice(self.suits)

    def get_card_icon(self):
        # this method return a tuple
        return random.choice(self.rank), random.choice(self.suits_icons)
