def create_inventory(items):
    mapa = {}
    for item in items:
        if item in mapa:
            mapa[item] = mapa[item]+1
        if item not in mapa:
            mapa[item] = 1
    return mapa


def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        if item not in inventory:
            inventory[item] = 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            if inventory[item] >0:  
                inventory[item] = inventory[item] - 1
        if item not in inventory:
            inventory[item] = item
    return inventory 


def remove_item(inventory, item):
    if item in inventory:
       del inventory[item]
    return inventory


def list_inventory(inventory):
    lista = []
    for item in inventory:
        if inventory[item] > 0:
            lista.append((item, inventory[item]))
    return lista
