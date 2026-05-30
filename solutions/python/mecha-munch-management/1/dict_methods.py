def add_item(current_cart: dict, items: list) -> dict:
    """Add an item to the shopping cart.

    Args:
        current_cart: A dictionary representing the current shopping cart.
        items: A list of items to add to the cart.

    Returns:
        A dictionary representing the updated shopping cart.
    """
    for item in items:
        if item not in current_cart:
            current_cart[item] = 1
        else:
            current_cart[item] += 1
    return current_cart

def read_notes(notes: list) -> dict:
    """Read a list of notes and return them as a list of strings.

    Args:
        notes: A list of notes to read."""
    note_dict = {}
    for note in notes:
        if note not in note_dict:
            note_dict[note] = 1
        else:
            note_dict[note] += 1    
    return note_dict    

def update_recipes(ideas: dict, recipe_updates) -> dict:
    for recipe_name, ingredients in recipe_updates:
        ideas[recipe_name] = ingredients

    return ideas

def sort_entries(cart: dict) -> dict:
    """Sort the entries in a shopping cart.

    Args:
        cart: A dictionary representing the shopping cart.

    Returns:
        A list of the sorted entries.
    """
    sorted_cart = dict(sorted(cart.items()))

    return sorted_cart

def send_to_store(cart:dict, aisle_mapping: dict) -> dict:
    """Send the shopping cart to the store, mapping items to their respective aisles.

    Args:
        cart: A dictionary representing the shopping cart.
        aisle_mapping: A dictionary mapping item names to their respective aisles in the store."""
    
    fulfillment_cart = {k: [cart[k]] + aisle_mapping[k] for k in cart if k in aisle_mapping}

    return dict(sorted(fulfillment_cart.items(), reverse=True))

def update_store_inventory(fulfillment_cart: dict, store_inventory: dict) -> dict:
    """Update the store inventory based on the items sold.

    Args:
        fulfillment_cart: A dictionary representing the fulfillment cart.
        store_inventory: A dictionary of items in the store inventory.

    Returns:
        A dictionary representing the updated store inventory.
    """
    for item in fulfillment_cart:
        if item in store_inventory:
            store_inventory[item][0] -= fulfillment_cart[item][0]
            if store_inventory[item][0] == 0:
                store_inventory[item][0] = "Out of Stock"
    
    return store_inventory



