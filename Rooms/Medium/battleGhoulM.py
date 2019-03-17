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
    baseM.showText(player, "You encountered a {}!".format(wording[0]),screen)
    choice = baseM.showText(player, "What do you do? [Fight, Run]\n",screen)
    if choice.title() in ["Fight", "F"]:
        baseM.showText(player, "You engage the {} in combat!".format(wording[1]),screen)
        baseM.runBasicFight(screen, player, enemies)
    elif choice.title() in ["Run", "Flee", "R"]:
        baseM.showText(player, "As you fearfully flee the angry {}, {} you, dealing {} damage.".format(wording[1],wording[2],7*len(enemies)),screen)
        player.health -= 7*len(enemies)
    else:
        baseM.checkCommands(choice, player,screen)
        run(player, (enemies, wording))
    return player

def test():
    theplayer = PChar()
    run(theplayer)
























