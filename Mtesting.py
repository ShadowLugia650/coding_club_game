import sys
sys.path.insert(0, "dependencies")
from itemStats import *
from curseScript import *

def specials(Input, player):
    if "addItem " in Input:
        itm = Input.split("addItem ")[1]
        try:
            player.items.append(eval(itm)())
        except NameError:
            pass
    elif "setHealth " in Input:
        health = Input.split("setHealth ")[1]
        player.health = int(health)
    elif "setGold " in Input:
        gold = Input.split("setGold ")[1]
        player.gold = int(gold)
    elif "addCurse " in Input:
        curse = Input.split("addCurse ")[1]
        try:
            player.curses.append(eval(curse)())
        except NameError:
            pass





