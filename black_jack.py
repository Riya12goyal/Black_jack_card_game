from cards_black_jack import logo
from cards_black_jack import card
from cards_black_jack import card_10
import os
import random

os.system("cls")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def display(user):
    for i in user:
        if i == 11 or i == 1:
            print(card[0], end = "" )
        elif i > 1 and i <10:
            print(card[i-1], end = "")
        elif i == 10:
            print(random.choice(card_10), end = "")

    print("]")

def result(sum_player, sum_computer):
    diff_player = 21 - sum_player
    diff_computer = 21 - sum_computer

    if sum_computer == 21:
        print("Lose, the oppenent has a black jack")
    elif sum_player == 21:
        print("Win with a blackjack")
    elif sum_player >21:
        print("You lose!")
        print("The sum exceeds 21")
    elif sum_computer >21:
        print("Opponent went over, You win :)")
    elif diff_computer < diff_player or (diff_player < 0):
        print("Computer wins!")
        print("Try Again!")
    elif diff_computer < diff_player:
        print("You win!")
    else:
        print("DRAW")

again = 'y'
while again == 'y':
    print("\t\t\tWELCOME TO THE GAME")
    print(logo)
    computer = []
    player = []
    for i in range(2):
        computer.append(random.choice(cards))
        player.append(random.choice(cards))

    print(f"Your cards are:", end = "" )
    display(player)
    print(f"current score:{sum(player)} ")
    print(f"Computer's first card:{computer[0]}")
    choice = input("Type 'y' to get another card or 'n' to pass:\t")
    while choice == 'y':
        card3 = int(random.choice(cards))
        player.append(card3)

        if 11 in player and sum(player) > 21:
            player.remove(11)
            player.append(1)
        print(f"Your cards are: [", end = "" )
        display(player)
        print(f"Current score: {sum(player)}")
        print(f"Computer's first card:{computer[0]}")
        choice = input("Type 'y' to get another card or 'n' to pass:\t")

    while sum(computer) < 17:
        computer_card3 = int(random.choice(cards))
        computer.append(computer_card3)

    sum_player = sum(player)
    sum_computer = sum(computer)
    print(f"Your final hand: [ ", end = "")
    display(player)
    print("Computer's final hand: [", end = "")
    display(computer)

    result(sum_player , sum_computer)
    again = input("Do you want to play Blackjack again? Type 'y' or 'n'")