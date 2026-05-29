def create_inventory(inventory : list) -> dict:
    inventory_dict= {}
    for item in inventory:
        if item in inventory_dict:
            inventory_dict[item] += 1
        else:
            inventory_dict[item] = 1
    return inventory_dict

def add_items(inventory_dict: dict, items: list) -> dict:
    for item in items:
        if item in inventory_dict:
            inventory_dict[item] += 1
        else:
            inventory_dict[item] = 1
    return inventory_dict

def decrement_items(inventory_dict: dict, items: list) -> dict:
    for item in items:
        if item in inventory_dict and inventory_dict[item] > 0:
            inventory_dict[item] -= 1
    return inventory_dict

def remove_item(inventory_dict: dict, item: str) -> dict:
    if item in inventory_dict:
        del inventory_dict[item]
    return inventory_dict   

def list_inventory(inventory_dict: dict) -> list:
    inventory_list = []
    for item, count in inventory_dict.items():
        if count > 0:
            inventory_list.append((item, count))
    return inventory_list
