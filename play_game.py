'''
Name: Alexander Zsikla
Date: 12/25/2019
play_game.py

Description:
'''

import card
import deck
import user
import dealer

def get_input():
    '''
    DOCSTRING:
    Input:
    Output:
    '''
    print("Actions:\n1. q --> quit\n2. s --> stay\n3. h --> hit")
    command = input("Please input an action: ").lower()

    while command != 'q' and command != 's' and command != 'h':
        print("That was not a valid command!")
        command = input("Please input an action: ").lower()

    return command

def betting(player):
    '''
    DOCSTRING:
    Input:
    Output:
    '''
    check_bet = True
    while check_bet:
        try:
            player_bet = int(input("Please enter an amount to bet: "))
        except:
            print("That is not a valid input")
        else:
            player.bet(player_bet)
            check_bet = False

def print_game(player, house):
    '''
    DOCSTRING:
    Input:
    Output:
    '''
    print("\n" * 100)
    print("YOU:\n{}\n\nDEALER:\n{}\n".format(str(player), str(house)))

def one_round(new):
    '''
    DOCSTRING:
    Input:
    Output:
    '''

    main_deck = deck.Deck()

    player1 = user.User(main_deck.deal_card(), main_deck.deal_card())
    player1.set_balance(new)
    house = dealer.Dealer(main_deck.deal_card(), main_deck.deal_card())

    player1.anti_up()
    print_game(player1, house)

    betting(player1)

    command = get_input()
    while command == 'h':
        player1.add_card(main_deck.deal_card())

        if player1.busted():
            print_game(player1, house)
            print("PLAYER BUSTED!!")
            return player1.get_balance()

        print_game(player1, house)

        command = get_input()

    house.switch_round()

    while not house.busted():
        if house.get_total() < 17:
            house.add_card(main_deck.deal_card())
            print_game(player1, house)
        else:
            break

    print_game(player1, house)
    if house.busted():
        print("DEALER BUSTED")
        player1.end_round(True)
    elif player1.get_total() > house.get_total():
        print("PLAYER WON!")
        player1.end_round(True)
    else:
        print("DEALER WON")
        player1.end_round(False)

    return player1.get_balance()

def game():
    '''
    DOCSTRING:
    Input:
    Output:
    '''
    print("\n" * 100)
    print("Welcome to BlackJack!\nTo play, there is a 5 dollar anti")
    print("If you win, you win back double what you bet!!")
    print("Hope you are ready!!!\n")

    balance = 100
    while balance >= 5:
        balance = one_round(balance)

        if balance < 5:
            break

        another_round = input("Play another round? Y/N?\n")

        if another_round.lower() == 'n':
            print("Game Over!!")
            exit(0)

    print("You ran out of money!")
    again = input("Play again? Y/N?\n")

    if again.lower() == 'y':
        game()

if __name__ == "__main__":
    game()
    exit(0)