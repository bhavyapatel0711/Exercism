def value_of_card(card) -> int:
    """Determine the scoring value of a card.

    :param card: str - the face or suit of the card.
    :return: int - the scoring value of the card.
    """
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)
    
def higher_card(card_one, card_two):
    """Determine which card has a higher value.

    :param card_one: str - the face or suit of the first card.
    :param card_two: str - the face or suit of the second card.
    :return: str or tuple - the card with the higher value, or both if they are of equal value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return (card_one, card_two)
    
def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming Ace card.

    :param card_one: str - the face or suit of the first card.
    :param card_two: str - the face or suit of the second card.
    :return: int - the value of the upcoming Ace card (either 1 or 11).
    """
    if card_one == 'A' or card_two == 'A':
        return 1
    
    total_value = value_of_card(card_one) + value_of_card(card_two)
    
    if total_value <= 10:
        return 11
    else:
        return 1    
    
def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'blackjack'.

    :param card_one: str - the face or suit of the first card.
    :param card_two: str - the face or suit of the second card.
    :return: bool - True if the hand is a blackjack, False otherwise.
    """
    return (value_of_card(card_one) == 10 and card_two == 'A') or (value_of_card(card_two) == 10 and card_one == 'A')

def can_split_pairs(card_one, card_two) -> bool:
    """Determine if a player can split their hand into two pairs.

    :param card_one: str - the face or suit of the first card.
    :param card_two: str - the face or suit of the second card.
    :return: bool - True if the hand can be split into pairs, False otherwise.
    """
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two) -> bool:
    """Determine if a player can place a double down bet.

    :param card_one: str - the face or suit of the first card.
    :param card_two: str - the face or suit of the second card.
    :return: bool - True if the hand can be doubled down on, False otherwise.
    """
    total_value = value_of_card(card_one) + value_of_card(card_two)
    return total_value in [9, 10, 11]   