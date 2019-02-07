import sys, random

sys.path.insert(0, 'dependencies')
import baseM
from itemStats import basicSword, basicDefensiveItem

def listItems(items):
    print("This shop has:")
    for i in items:
        print('{}: {}'.format(i, items[i]))

def run(player):
    items = {}
    allItems = {"Sword":(basicSword(),50), "Shield":(basicDefensiveItem(),50), "Health Potion":(None,10)}
    for i in range(10):
        itm = random.choice(list(allItems.keys()))
        items[itm] = allItems[itm]
    print("Welcome, Traveller! Buy something at my shop!")
    choice = input("What do you do? [Buy, Leave]\n")
    if choice.title() in ["Buy", "B"]:
        listItems(items)
        im = None
        while im not in ["Leave", "L"]:
            im = input("What would you like to buy? (type 'Leave' to leave).\n")
            im = im.title()
            if im in ["Leave", "L"]:
                break
            elif im not in list(items.keys()):
                print("This shop doesn't have that...")
            elif items[im][1] > player.gold:
                print(random.choice(["You don't have enough money for that..", "Don't be a thief!"]))
            else:
                print("You bought a {}".format(im))
                player.gold -= items[im][1]
                player.items.append(items[im][0])
                items.pop(im)
    elif choice.title() in ["Leave", "L"]:
        print("You walk past this 'shop' and continue your journey...")
    else:
        baseM.checkCommands(choice, player)
        run(player)
    return player
