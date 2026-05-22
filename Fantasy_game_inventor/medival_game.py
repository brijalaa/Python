stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v , k)
        item_total += v
        # FILL THIS PART IN
    print("Total number of items: " + str(item_total))

def add_to_inventory(inventory, added_items):
    for i in added_items:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory
    # Your code goes here.

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)


display_inventory(stuff)
