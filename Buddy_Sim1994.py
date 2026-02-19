import random
import time
import math

namebuddy = input("Welcome to Buddy Sim 1994! What's my name?")

def make_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']
    return [r + s for r in ranks for s in suits]


def hand_value(hand):
    values = 0
    aces = 0
    for card in hand:
        rank = card[:-1]
        if rank in ['J', 'Q', 'K']:
            values += 10
        elif rank == 'A':
            aces += 1
            values += 11
        else:
            values += int(rank)

    while values > 21 and aces:
        values -= 10
        aces -= 1
    return values


def draw(deck):
    if not deck:
        deck.extend(make_deck())
        random.shuffle(deck)
    return deck.pop()


def show_hand(hand):
    return ' '.join(hand)


def play_jackblack():
    deck = make_deck()
    random.shuffle(deck)

    while True:
        player = [draw(deck), draw(deck)]
        dealer = [draw(deck), draw(deck)]

        print("GET READY FOR ANOTHER ROUND!")
        print(f"Dealer shows: {dealer[0]}")
        print(f"Your hand: {show_hand(player)} (value: {hand_value(player)})")

        # Player turn
        while True:
            if hand_value(player) == 21:
                print("Blackjack! You win!")
                break
            move = input("Hit or stand? (h/s): ").strip().lower()
            if move == 'h':
                player.append(draw(deck))
                print(f"You drew: {player[-1]}")
                print(f"Your hand: {show_hand(player)} (value: {hand_value(player)})")
                if hand_value(player) > 21:
                    print("You busted!")
                    break
            elif move == 's':
                break
            else:
                move = input("Please enter 'h' to hit or 's' to stand.")

        # Dealer turn, simple AI, hits until 17
        player_val = hand_value(player)
        dealer_val = hand_value(dealer)
        print(f"\nDealer reveals: {show_hand(dealer)} (value: {dealer_val})")
        if player_val <= 21:
            while dealer_val < 17:
                dealer.append(draw(deck))
                dealer_val = hand_value(dealer)
                print(f"Dealer draws: {dealer[-1]} -> value {dealer_val}")

        # Outcome
        print('\n--- Result ---')
        print(f"Your hand: {show_hand(player)} -> {player_val}")
        print(f"Dealer hand: {show_hand(dealer)} -> {dealer_val}")

        if player_val > 21:
            print("You lose (bust)!")
        elif dealer_val > 21:
            print("Dealer busts — you win!")
        elif player_val > dealer_val:
            print("You win!")
        elif player_val < dealer_val:
            print("You lose!")
        else:
            print("Push (tie)!")
        
        while True:
            again = input("Play again? (y/n): ").strip().lower()
            if again == 'y':
                break
            elif again == 'n':
                return
            else:
                print("Please input 'y' to play again or 'n' to exit.")

        
def play_rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        player_choice = input("Rock, paper, or scissors? (r/p/s): ").strip().lower()
        
        if player_choice == 'r':
            player_choice = 'rock'
        elif player_choice == 'p':
            player_choice = 'paper'
        elif player_choice == 's':
            player_choice = 'scissors'
        else:
            print("Please enter 'r', 'p', or 's'.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"You chose: {player_choice}, I chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")
        
        while True:
            again = input("Play again? (y/n): ").strip().lower()
            if again == 'y':
                break
            elif again == 'n':
                return
            else:
                print("Please input 'y' to play again or 'n' to exit.")


def play_guess_the_number():
    while True:
        secret = random.randint(1, 100)
        guesses = 0
        
        print("I'm thinking of a number between 1 and 100...")
        
        while True:
            try:
                guess = int(input("What's your guess? "))
                guesses += 1
                
                if guess < secret:
                    print("Too low!")
                elif guess > secret:
                    print("Too high!")
                else:
                    print(f"You got it! The number was {secret}. It took you {guesses} guesses!")
                    break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            again = input("Play again? (y/n): ").strip().lower()
            if again == 'y':
                break
            elif again == 'n':
                return
            else:
                print("Please input 'y' to play again or 'n' to exit.")


def main_menu():
    while True:
        gamenum = int(input(f"Whew! I had forgotten my name for a second (How'd I do that?)! \nBut yes, {namebuddy} is definetely my name. \nNow, let's play some games! \nEnter 1 for JackBlack, \nEnter 2 for Rock, Paper, Scissors, \nand 3 for guess the number!"))
        
        if gamenum == 1:
            play_jackblack()
        elif gamenum == 2:
            play_rock_paper_scissors()
        elif gamenum == 3:
            play_guess_the_number()
        else:
            print("Other game not implemented yet! Please choose 1, 2, or 3 next time.")

main_menu()