"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in ("J","Q","K"):
        return 10
    if card=="A":
        return 1
    return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one,card_two
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    return card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the next Ace to be drawn."""
    # If you already have an Ace, the new one must be 1
    if card_one == "A" or card_two == "A":
        return 1

    # Otherwise, calculate total of the two cards
    total_value = value_of_card(card_one) + value_of_card(card_two)
    if total_value <= 10:
        return 11
    return 1

def is_blackjack(card_one, card_two):
    """Return True if the hand is a natural blackjack (Ace + 10-value card)."""
    if (card_one == "A" and value_of_card(card_two) == 10):
        return True
    elif (card_two == "A" and value_of_card(card_one) == 10):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    if higher_card(card_one,card_two) == (card_one,card_two):
        return True
    return False

def can_double_down(card_one, card_two):
    total_value = value_of_card(card_one) + value_of_card(card_two)

    # Exclude two Aces from doubling down
    if card_one == "A" and card_two == "A":
        return False

    # Rule: can double down if total value is 9, 10, or 11
    if total_value in (9, 10, 11):
        return True
    return False