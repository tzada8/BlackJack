# Each card has a name, a worth, an alt worth (only if an ace), and a quality of whether it is a face card/an ace
class Card:

    def __init__(self, name, worth, alt_worth, is_face_card, is_ace):
        self.name = name  # Name of card
        self.worth = worth  # Worth of card in BlackJack
        self.alt_worth = alt_worth  # Alternate worth of a card (for Aces)
        self.is_face_card = is_face_card  # Boolean if card is a face card
        self.is_ace = is_ace  # Boolean if card is an ace


# 1-13 are spades
# 14-26 are diamonds
# 27-39 are hearts
# 40-52 are clubs
# Every 13 cards, the number repeats (e.g. 1 and 14 are both an "Ace")

# Each number from 1 to 52 is mapped to a specific Card object in a deck of cards with all corresponding features
card_mapping = {
    1: Card("ace_of_spades", 11, 1, False, True),  # All spades
    2: Card("2_of_spades", 2, None, False, False),
    3: Card("3_of_spades", 3, None, False, False),
    4: Card("4_of_spades", 4, None, False, False),
    5: Card("5_of_spades", 5, None, False, False),
    6: Card("6_of_spades", 6, None, False, False),
    7: Card("7_of_spades", 7, None, False, False),
    8: Card("8_of_spades", 8, None, False, False),
    9: Card("9_of_spades", 9, None, False, False),
    10: Card("10_of_spades", 10, None, False, False),
    11: Card("jack_of_spades", 10, None, True, False),
    12: Card("queen_of_spades", 10, None, True, False),
    13: Card("king_of_spades", 10, None, True, False),

    14: Card("ace_of_diamonds", 11, 1, False, True),  # All diamonds
    15: Card("2_of_diamonds", 2, None, False, False),
    16: Card("3_of_diamonds", 3, None, False, False),
    17: Card("4_of_diamonds", 4, None, False, False),
    18: Card("5_of_diamonds", 5, None, False, False),
    19: Card("6_of_diamonds", 6, None, False, False),
    20: Card("7_of_diamonds", 7, None, False, False),
    21: Card("8_of_diamonds", 8, None, False, False),
    22: Card("9_of_diamonds", 9, None, False, False),
    23: Card("10_of_diamonds", 10, None, False, False),
    24: Card("jack_of_diamonds", 10, None, True, False),
    25: Card("queen_of_diamonds", 10, None, True, False),
    26: Card("king_of_diamonds", 10, None, True, False),

    27: Card("ace_of_hearts", 11, 1, False, True),  # All hearts
    28: Card("2_of_hearts", 2, None, False, False),
    29: Card("3_of_hearts", 3, None, False, False),
    30: Card("4_of_hearts", 4, None, False, False),
    31: Card("5_of_hearts", 5, None, False, False),
    32: Card("6_of_hearts", 6, None, False, False),
    33: Card("7_of_hearts", 7, None, False, False),
    34: Card("8_of_hearts", 8, None, False, False),
    35: Card("9_of_hearts", 9, None, False, False),
    36: Card("10_of_hearts", 10, None, False, False),
    37: Card("jack_of_hearts", 10, None, True, False),
    38: Card("queen_of_hearts", 10, None, True, False),
    39: Card("king_of_hearts", 10, None, True, False),

    40: Card("ace_of_clubs", 11, 1, False, True),  # All clubs
    41: Card("2_of_clubs", 2, None, False, False),
    42: Card("3_of_clubs", 3, None, False, False),
    43: Card("4_of_clubs", 4, None, False, False),
    44: Card("5_of_clubs", 5, None, False, False),
    45: Card("6_of_clubs", 6, None, False, False),
    46: Card("7_of_clubs", 7, None, False, False),
    47: Card("8_of_clubs", 8, None, False, False),
    48: Card("9_of_clubs", 9, None, False, False),
    49: Card("10_of_clubs", 10, None, False, False),
    50: Card("jack_of_clubs", 10, None, True, False),
    51: Card("queen_of_clubs", 10, None, True, False),
    52: Card("king_of_clubs", 10, None, True, False)
}
