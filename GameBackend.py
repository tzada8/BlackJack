import random as rndm

from Competitor import user, dealer
from Card import card_mapping


# --- BACKEND FUNCTIONS ---


# Resets cards back such that all 52 cards can be selected from for following round
def shuffle_deck():
    deck = list(range(1, 53))  # List of ordered numbers: 1 to 52
    rndm.shuffle(deck)  # Shuffles List to a random order
    return deck


# Deals top 4 cards of deck; 2 cards to user, 2 cards to dealer
def deal_starter_cards(all_cards):
    user.cards = [card_mapping.get(all_cards.pop())]  # First card is user's
    dealer.cards = [card_mapping.get(all_cards.pop())]  # Second card is dealer's
    user.cards.append(card_mapping.get(all_cards.pop()))  # Third card is user's
    dealer.cards.append(card_mapping.get(all_cards.pop()))  # Fourth card is dealer's


# Calculates most optimal hand for all competitors
def calc_hand_worth(person):
    hand_worth = 0
    for card in person.cards:  # For loop that finds worth of hand (assuming Ace's are 11)
        hand_worth = hand_worth + card.worth

    # If calculated to have over 21 and person has Aces,
    # then switch all Aces to their alt value (1 instead of 11)
    if hand_worth > 21:
        for card in person.cards:
            if card.is_ace:
                # Decrease 11 for original Ace value, and increase 1 for new value
                hand_worth = hand_worth - card.worth + card.alt_worth

    # If newly calculated value is less than or equal to 11, then can afford to make 1 Ace revert
    # back to original value of 11
    if hand_worth <= 11:
        for card in person.cards:
            if card.is_ace:
                hand_worth = hand_worth + card.worth - card.alt_worth
                return hand_worth

    return hand_worth


# Compares hand worth for both dealer and user, and determines who won / if a tie
def determine_winner(user_hand, dealer_hand):
    if user_hand > 21:  # User busted
        winner = "bust"
    elif user_hand < dealer_hand <= 21:  # Dealer wins
        winner = "dealer"
    elif dealer_hand == user_hand and dealer_hand <= 21 and user_hand <= 21:  # Tie, unless someone has BlackJack
        if has_blackjack(user) and has_blackjack(dealer):
            winner = ""
        elif has_blackjack(user):
            winner = "user"
        elif has_blackjack(dealer):
            winner = "dealer"
        else:
            winner = ""
    elif dealer_hand < user_hand <= 21:  # User wins
        winner = "user"
    elif dealer_hand > 21:  # Dealer busts
        winner = "user"
    elif user_hand < 21:  # User busts
        winner = "dealer"
    else:
        winner = ""

    return winner


# Determines if person has BlackJack, returning T/F accordingly
def has_blackjack(person):
    # Go through cards person has and if: there are 2 cards, 1 is Ace, 1 is Face card, then return True
    return (len(person.cards) == 2) and (  # If person has 2 cards, AND
            (person.cards[0].is_ace and person.cards[1].is_face_card) or (  # Ace 1st card, Face 2nd, OR
            person.cards[1].is_ace and person.cards[0].is_face_card))  # Ace 2nd card, Face 1st


# Function that allows a button to run multiple commands
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func


# Variables that keep track of users stats to be output when user cash's out/loses game
hands_won = 0
total_cash_won = 0
highest_bank = 1000
