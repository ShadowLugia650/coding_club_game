import sys, random

sys.path.insert(0, 'dependencies')
import baseM
from itemStats import *

def listItems(items):
    baseM.showText("This shop has:",screen)
    for i in items:
        baseM.showText('{}: {}'.format(i, items[i]),screen)

def run(player, screen):
    items = {}
    allItems = {sword():100, shield():100, healthPotion():20, antidote():80, armoredShirt():150, torch():35, orbOfThunder():50}
    for i in range(10):
        itm = random.choice(list(allItems.keys()))
        items[itm] = allItems[itm]
    baseM.showText("Welcome, Traveller! Buy something at my shop!",screen)
    choice = baseM.showText("What do you do? [Buy, Leave]\n",screen)
    if choice.title() in ["Buy", "B"]:
        listItems(items)
        im = None
        while im not in ["leave", "l"]:
            im = baseM.showText("What would you like to buy? (type 'Leave' to leave,screen).\n",screen)
            im = baseM.strToClsNm(im)
            found = False
            if im in ["leave", "l"]:
                break
            for i in list(items.keys()):
                if baseM.strToClsNm(i.name) == im:
                    found = True
                    if items[i] > player.gold:
                        baseM.showText(random.choice(["You don't have enough money for that..", "Don't be a thief!"]),screen)
                    else:
                        try:
                            itm = eval(im)()
                            baseM.showText("You bought a {}".format(itm),screen)
                            player.gold -= items[i]
                            player.items.append(itm)
                            items.pop(i)
                        except NameError:
                            baseM.showText("Are you sure that's an item?",screen)
                            itm = None
            if not found:
                baseM.showText("This shop doesn't have that.",screen)
            baseM.checkCommands(im, player,screen)
    elif choice.title() in ["Leave", "L"]:
        baseM.showText("You walk past this 'shop' and continue your journey...",screen)
    else:
        baseM.checkCommands(choice, player,screen)
        run(player, screen)
    return player







