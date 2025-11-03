"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    round_list=[number,number+1,number+2]
    return round_list
    


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    combined_list=rounds_1+rounds_2
    return combined_list


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    return False


def card_average(hand):
    return sum(hand)/len(hand) 

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    first_num = hand[0]
    last_num = hand[-1]
    avg_fl=(first_num+last_num)/2
    if len(hand) % 2 == 1:
        middle_card = hand[len(hand) // 2]
    else:
        middle_card = None  # No middle card for even-sized lists
    
    true_avg = card_average(hand)  # Calculate true average of all cards
    print(card_average(hand))
    print(avg_fl)
    if true_avg == avg_fl or middle_card == true_avg:
        return True
    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_list=[]
    odd_list=[]
    for index, n in enumerate(hand):  # Enumerate to get index and value
        if index % 2 == 0:  # Even index
            even_list.append(n)
        else:  # Odd index
            odd_list.append(n)

    # Compare the averages of even and odd indexed numbers
    if card_average(even_list) == card_average(odd_list):
        return True
    return False



def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    double_last=hand[-1]
    if double_last == 11:
        hand.pop()
        hand.append(22)
    return hand
        