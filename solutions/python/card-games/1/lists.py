def get_rounds(round_number: int) -> list:
    """Return a list of rounds including round_number and the two rounds before and after it."""
    return [ round_number, round_number + 1, round_number + 2]

def concatenate_rounds(rounds_1: list, rounds_2: list) -> list:
    """Concatenate two lists of rounds together."""
    return rounds_1 + rounds_2  

def list_contains_round(rounds: list, round_number: int) -> bool:   
    """Check if the list of rounds contains the specified round_number."""
    return round_number in rounds

def card_average(hand: list) -> int:
    """Calculate and return the average card value from the hand."""
    return sum(hand) / len(hand)

def approx_average_is_average(hand: list) -> bool:
    """Check if the approximate average (first + last card / 2) is equal to the actual average."""
    actual_average = card_average(hand)
    approx_average = (hand[0] + hand[-1]) / 2
    return actual_average == approx_average or actual_average == hand[len(hand) // 2]

def average_even_is_average_odd(hand: list) -> bool:
    """Check if the average of even indexed cards is equal to the average of odd indexed cards."""
    even_indexed_cards = hand[::2]
    odd_indexed_cards = hand[1::2]
    average_even = card_average(even_indexed_cards)
    average_odd = card_average(odd_indexed_cards)
    return average_even == average_odd

def maybe_double_last(hand: list) -> list:
    """Double the value of the last card if it is a Jack (11)."""
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
