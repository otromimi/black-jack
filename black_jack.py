import deck
import players
from console_interface import *

print("Welcome to black Jack mimi\n\n")


class Hand:
    # Players initialization
    Dealer = players.Dealer()
    Player_0 = players.Gambler(100)
    # Deck of card to play with
    Deck = deck.Deck()

    def set_up(self):
        # New hand set-up
        self.Player_0.new_hand()
        self.Dealer.new_hand()
        # Gambler bet
        #self.Player_0.deal(ask_for_bet())
        self.Player_0.deal(10)
        # Dealing starting cards
        self.Player_0.hit(self.Deck.get_card_icon())
        self.Dealer.hit(self.Deck.get_card_icon())
        self.Player_0.hit(self.Deck.get_card_icon())
        self.Dealer.hit(self.Deck.get_card_icon())
        # Print status
        print_status(self.Dealer.get_cards(), '', self.Player_0.get_cards(), self.Player_0.card_count())
        self.gamblers_turn()

    def gamblers_turn(self):
        playing = True
        while playing and self.Player_0.card_count() <= 21:
            playing = hit()
            if playing:
                self.Player_0.hit(self.Deck.get_card_icon())
                print_status(self.Dealer.get_cards(), '', self.Player_0.get_cards(), self.Player_0.card_count())
        self.dealer_turn()

    def dealer_turn(self):
        print_status(self.Dealer.show_cards(), self.Dealer.card_count(), self.Player_0.get_cards(), self.Player_0.card_count())
        passed = self.Dealer.pass_table_min()
        while not passed:
            self.Dealer.hit(self.Deck.get_card_icon())
            passed = self.Dealer.pass_table_min()
        print_status(self.Dealer.show_cards(), self.Dealer.card_count(), self.Player_0.get_cards(), self.Player_0.card_count())
        if (self.Player_0.card_count() <= 21 and self.Player_0.card_count() > self.Dealer.card_count()) or self.Dealer.card_count() > 21:
            print("You won")
        else:
            print("You lost")



Game = Hand()

other = True
while other:
    Game.set_up()
    other=another_hand()
