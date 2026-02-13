import random
import time
import math

namebuddy = input("Welcome to Buddy Sim 1994! What's my name?")

gamenum = int(input(f"Whew! I had forgotten my name for a second (How'd I do that?)! \nBut yes, {namebuddy} is definetely my name. \nNow, let's play some games! \nEnter 1 for JackBlack, \nEnter 2 for Rock, Paper, Scissors, \nand 3 for the other"))



# --- Basic Blackjack implementation (extremely simple) ---

def make_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']
    return [r + s for r in ranks for s in suits]


def hand_value(hand):
    # Returns best Blackjack value for hand (Aces counted as 1 or 11)
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
    # Downgrade Aces from 11 to 1 as needed
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
    return ' '.jo in(hand)


def play_jackblack():
    deck = make_deck()
    random.shuffle(deck)

    while True:
        player = [draw(deck), draw(deck)]
        dealer = [draw(deck), draw(deck)]

        print("\nNew Round! GET READY FOR ANOTHER ROUND!")
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
                print("Please enter 'h' to hit or 's' to stand.")

        # Dealer turn
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
            print("You lose (bust).")
        elif dealer_val > 21:
            print("Dealer busts — you win!")
        elif player_val > dealer_val:
            print("You win!")
        elif player_val < dealer_val:
            print("You lose.")
        else:
            print("Push (tie).")

        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing Blackjack!")
            break


if gamenum == 1:
    play_jackblack()
elif gamenum == 2:
    print("Rock, Paper, Scissors not implemented — choose 1 to play Blackjack.")
else:
    print("Other game not implemented.")