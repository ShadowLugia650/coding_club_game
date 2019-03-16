import sys, random

sys.path.insert(0, 'dependencies')
import baseM
from itemStats import *

def listItems(items):
    baseM.showText("This shop has:")
    for i in items:
        baseM.showText('{}: {}'.format(i, items[i]))

def run(player, screen):
    items = {}
    allItems = {sword():100, shield():100, healthPotion():20, antidote():80, armoredShirt():150, torch():35, orbOfThunder():50}
    for i in range(10):
        itm = random.choice(list(allItems.keys()))
        items[itm] = allItems[itm]
    baseM.showText("Welcome, Traveller! Buy something at my shop!")
    choice = input("What do you do? [Buy, Leave]\n")
    if choice.title() in ["Buy", "B"]:
        listItems(items)
        im = None
        while im not in ["leave", "l"]:
            im = input("What would you like to buy? (type 'Leave' to leave).\n")
            im = baseM.strToClsNm(im)
            found = False
            if im in ["leave", "l"]:
                break
            for i in list(items.keys()):
                if baseM.strToClsNm(i.name) == im:
                    found = True
                    if items[i] > player.gold:
                        baseM.showText(random.choice(["You don't have enough money for that..", "Don't be a thief!"]))
                    else:
                        try:
                            itm = eval(im)()
                            baseM.showText("You bought a {}".format(itm))
                            player.gold -= items[i]
                            player.items.append(itm)
                            items.pop(i)
                        except NameError:
                            baseM.showText("Are you sure that's an item?")
                            itm = None
            if not found:
                baseM.showText("This shop doesn't have that.")
            baseM.checkCommands(im, player)
    elif choice.title() in ["Leave", "L"]:
        baseM.showText("You walk past this 'shop' and continue your journey...")
    else:
        baseM.checkCommands(choice, player)
        run(player, screen)
    return player


