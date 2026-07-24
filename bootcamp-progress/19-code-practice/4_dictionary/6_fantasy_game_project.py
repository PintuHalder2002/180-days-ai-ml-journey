'''
List	to	Dictionary	Function	for	Fantasy	Game
Inventory
Imagine	that	a	vanquished	dragon’s	loot	is	represented	as	a	list	of	strings	like
this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write	a	function	named	addToInventory(inventory, addedItems),	where
the	inventory	parameter	is	a	dictionary	representing	the	player’s	inventory	(like
in	the	previous	project)	and	the	addedItems	parameter	is	a	list	like	dragonLoot.
The	addToInventory()	function	should	return	a	dictionary	that	represents	the
updated	inventory.	Note	that	the	addedItems	list	can	contain	multiples	of	the
same	item.	Your	code	could	look	something	like	this:
'''



def displayInventory(inventory):
    print("Inventory:")
    item_total = 0

    for k, v in inventory.items():
        # FILL THIS PART IN
        print(v ," ",k)
        item_total += int(v)

    print("Total number of items: " + str(item_total))
    return inventory



def addToInventory(inv, dragonLoot):
    # your code goes here
    for i in dragonLoot:
        if i not in inv.keys():
            inv.setdefault(i , 1)  # use setdefault instead of get because get will not create the absent items(which is present in the list) in the dictionary.
        else:
            inv[i] += 1
    return inv


'''
shortcut method

def addToInventory(inv, dragonLoot):
    # your code goes here
    for i in dragonLoot:
        inv.setdefault(i , 1)  # use setdefault instead of get because get will not create the absent items(which is present in the list) in the dictionary.
        inv[i] += 1
    return inv
'''


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

'''
The	previous	program	(with	your	displayInventory()	function	from	the
previous	project)	would	output	the	following:
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48
'''
