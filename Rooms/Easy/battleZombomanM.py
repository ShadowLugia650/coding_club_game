import random, sys

sys.path.insert(0, "dependencies")
import baseM
from baseM import Zomboman

def run(player, screen):
    baseM.showText("You encountered a Zombo-man!",screen)
    enemies = [Zomboman()]
    for itm in player.items:
        if itm.name == "Zomboman Guts":
            enemies.append(Zomboman())
    choice = baseM.showText("What do you do? [Fight, Run]\n",screen)
    if choice.title() in ["Fight", "F"]:
        baseM.showText("You engage the Zombo-man in combat!",screen)
        baseM.runBasicFight(player, enemies)
    elif choice.title() in ["Run", "Flee", "R"]:
        baseM.showText("As you fearfully flee the angry Zombo-man, it punches you, dealing 1 damage.",screen)
        player.health -= 1
    else:
        baseM.checkCommands(choice, player)
        run(player, screen)
    return player






