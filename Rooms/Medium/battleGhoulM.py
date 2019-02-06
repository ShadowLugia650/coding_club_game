import sys, random

sys.path.insert(0, 'dependencies')
import baseM
from baseM import Ghoul
from pScript import PChar

def run(player, setEnemies = None):
    if setEnemies is not None:
        enemies = setEnemies[0]
        wording = setEnemies[1]
    else:
        enemies = [Ghoul()]
        wording = []
        rng = random.randint(1, 100)
        if rng <= 15:
            for i in range(3):
                enemies.append(Ghoul())
            wording = ["horde of ghouls", "ghouls", "they hit"]
        else:
            wording = ["ghoul", "ghoul", "it hits"]
    print("You encountered a {}!".format(wording[0]))
    choice = input("What do you do? [Fight, Run]\n")
    if choice.title() in ["Fight", "F"]:
        print("You engage the {} in combat!".format(wording[1]))
        baseM.runBasicFight(player, enemies)
    elif choice.title() in ["Run", "Flee", "R"]:
        print("As you fearfully flee the angry {}, {} you, dealing {} damage.".format(wording[1],wording[2],7*len(enemies)))
        player.health -= 7*len(enemies)
    else:
        baseM.checkCommands(choice, player)
        run(player, (enemies, wording))
    return player

def test():
    thePlayer = PChar()
    run(thePlayer)
