import sys, random

sys.path.insert(0, 'dependencies')
import baseM
from itemStats import *

def listItems(items):
    print("This shop has:")
    for i in items:
        print('{}: {}'.format(i, items[i]))

def run(player):
    items = {}
    allItems = {sword():50, shield():50, healthPotion():10}
    for i in range(10):
        itm = random.choice(list(allItems.keys()))
        items[itm] = allItems[itm]
    print("Welcome, Traveller! Buy something at my shop!")
    choice = input("What do you do? [Buy, Leave]\n")
    if choice.title() in ["Buy", "B"]:
        listItems(items)
        im = None
        while im not in ["leave", "l"]:
            im = input("What would you like to buy? (type 'Leave' to leave).\n")
            im = baseM.strToClsNm(im)
            if im in ["leave", "l"]:
                break
            itm = eval(im)()
            if itm not in list(items.keys()):
                print("This shop doesn't have that...")
            elif items[itm] > player.gold:
                print(random.choice(["You don't have enough money for that..", "Don't be a thief!"]))
            else:
                print("You bought a {}".format(itm))
                player.gold -= items[itm]
                player.items.append(itm)
                items.pop(itm)
    elif choice.title() in ["Leave", "L"]:
        print("You walk past this 'shop' and continue your journey...")
    else:
        baseM.checkCommands(choice, player)
        run(player)
    return player
