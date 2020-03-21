class Player:
    cards = []

    def get_cards(self):
        return self.cards

    def hit(self, card):
        self.cards.append(card)

    def stand(self):
        pass

    def double(self):
        pass

    def surrender(self):
        pass

    def new_hand(self):
        self.cards = []

    def card_count(self):
        counter = 0
        for i in self.cards:
            if 'J' == i[0] or 'Q' == i[0] or 'K' == i[0]:
                counter += 10
            elif 'A' == i[0]:
                counter += 11
            else:
                counter += int(i[0])

        for i in self.cards:
            if counter <= 21:
                break
            if i[0] == 'A':
                counter -= 10

        return counter


class Dealer(Player):
    min_dealer = 16

    def get_cards(self):
        return self.cards[0]

    def show_cards(self):
        return super().get_cards()

    def pass_table_min(self):
        return super().card_count() >= self.min_dealer


class Gambler(Player):
    bet = 0
    chips: int

    def __init__(self, money):
        self.chips = money

    def deal(self, bet):
        self.bet = bet
        self.chips -= self.bet

    def new_hand(self):
        self.bet = 0
        super().new_hand()

    def win(self):
        self.chips += (2 * self.bet)

    def win_blackjack(self):
        self.chips += (2.5 * self.bet)
