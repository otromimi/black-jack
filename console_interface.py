def another_hand():
    select = input("Do you want to play another hand? (Y/n): ")
    if select == '' or select.upper() == 'Y':
        return True
    else:
        return False


def print_status(dealer, dealer_points, player, player_points):
    print('-------------------------------------------------------')
    print(f"Dealer: {dealer}\t{dealer_points}")
    print(f"Player: {player}\t{player_points}")


def ask_for_bet():
    return int(input("Bet (integer): "))


def hit():
    select = input("Hit (Y/n): ")
    if select == '' or select.upper() == 'Y':
        return True
    else:
        return False
