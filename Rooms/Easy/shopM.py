import sys, random

sys.path.insert(0, 'dependencies')
import baseM
from itemStats import *

def listItems(items, screen):
    baseM.showText(None, "This shop has:",screen)
    for i in items:
        baseM.showText(None, '{}: {}'.format(i, items[i]),screen)

def run(player, screen):
    items = {}
    allItems = {sword():100, shield():100, healthPotion():20, antidote():80, armoredShirt():150, torch():35, orbOfThunder():50}
    for i in range(10):
        itm = random.choice(list(allItems.keys()))
        items[itm] = allItems[itm]
    baseM.showText(player, "Welcome, Traveller! Buy something at my shop!",screen)
    choice = baseM.showText(player, "What do you do? [Buy, Leave]\n",screen)
    if choice.title() in ["Buy", "B"]:
        listItems(items, screen)
        im = None
        while im not in ["leave", "l"]:
            im = baseM.showText(player, "What would you like to buy? (type 'Leave' to leave).\n",screen)
            im = baseM.strToClsNm(im)
            found = False
            if im in ["leave", "l"]:
                break
            for i in list(items.keys()):
                if baseM.strToClsNm(i.name) == im:
                    found = True
                    if items[i] > player.gold:
                        baseM.showText(player, random.choice(["You don't have enough money for that..", "Don't be a thief!"]),screen)
                    else:
                        try:
                            itm = eval(im)()
                            baseM.showText(player, "You bought a {}".format(itm),screen)
                            player.gold -= items[i]
                            player.items.append(itm)
                            items.pop(i)
                        except NameError:
                            baseM.showText(player, "Are you sure that's an item?",screen)
                            itm = None
            if not found:
                baseM.showText(player, "This shop doesn't have that.",screen)
            baseM.checkCommands(im, player,screen)
    elif choice.title() in ["Leave", "L"]:
        baseM.showText(player, "You walk past this 'shop' and continue your journey...",screen)
    else:
        baseM.checkCommands(choice, player,screen)
        run(player, screen)
    return player
