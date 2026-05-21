def exchange_money(budget: float, exchange_rate: float) -> float:
    """This function returns the amount of foreign currency you can receive."""
    return budget / exchange_rate

def get_change(budget: float, exchanging_value: float) -> float:
    """This function returns the amount of money you have left after exchanging.""" 
    return budget - exchanging_value    

def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """This function returns the total value of your bills."""
    return denomination * number_of_bills

def get_number_of_bills(amount: float, denomination: int) -> int:
    """This function returns the number of bills you can get."""
    return int(amount // denomination)      

def get_leftover_of_bills(budget: float, denomination: int) -> float:
    """This function returns the leftover amount that cannot be exchanged in bills."""
    return budget % denomination        

def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int: 
    """This function returns the maximum value of the new currency you can get."""
    exchange_rate_with_spread = exchange_rate * (1 + spread / 100)
    exchanged_amount = exchange_money(budget, exchange_rate_with_spread)
    number_of_bills = get_number_of_bills(exchanged_amount, denomination)
    return get_value_of_bills(denomination, number_of_bills)

