import random, sys

sys.path.insert(0, "dependencies")
import baseM
from baseM import Zomboman

def run(player):
    print("You encountered a Zombo-man!")
    enemies = [Zomboman()]
    choice = input("What do you do? [Fight, Run]\n")
    if choice.title() in ["Fight", "F"]:
        print("You engage the Zombo-man in combat!")
        baseM.runBasicFight(player, enemies)
    elif choice.title() in ["Run", "Flee", "R"]:
        print("As you fearfully flee the angry Zombo-man, it punches you, dealing 1 damage.")
        player.health -= 1
    else:
        baseM.checkCommands(choice, player)
        run(player)
    return player
