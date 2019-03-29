import sys
sys.path.insert(0, 'dependencies')
import pScript, console, baseM
from itemStats import glowingEyes

class Gargoyle(baseM.basicEnemy):
    def __init__(self):
        self.type = "Gargoyle"
        self.baseDamage = 10
        self.baseDef = 0
        self.block = 0
        self.health = 200
        self.maxHp = 200
        self.loot = [glowingEyes(), ("Gold", 45)]
        self.options = {"Whack":0, "Thwack":5, "Smack":-5, "Crack":0}

def run(player, screen):
    baseM.showText(player, "You enter a seemingly empty room. [continue]",screen)
    baseM.showText(player, "As you walk further in, you begin to feel dizzy.[continue]",screen)
    baseM.showText(player, "You see two doors at the end of the room.[continue]",screen)
    baseM.showText(player, "What do you do?",screen)
    while True:
        choice = baseM.showText(player, "[Go through left door, Go through right door, Leave]",screen)
        if choice.lower() in ["left", "left door", "go through left door"]:
            baseM.showText(player, "You start towards the left door when suddenly, your body moves toward the right door. [continue]",screen)
            baseM.showText(player, "You struggle to take control but it is too late. [continue]",screen)
            baseM.showText(player, "You enter the right door which reveals a golden goblet with a strange glowing liquid. [continue]",screen)
            while True:
                baseM.showText(player, "What do you do?",screen)
                choice = input ("[Drink the liquid, Leave]")
                if choice.lower() in ["drink", "liquid", "drink the liquid"]:
                    baseM.showText(player, "You drink the liquid and feel refreshed. You regain 30 health",screen)
                    pScript.heal (player,30)
                    break
                elif choice.lower() in ["leave"]:
                    baseM.showText(player, "You leave the room dumbfounded but unscathed",screen)
                    break
                else:
                    baseM.checkCommands(choice, player,screen)
            break
        elif choice.lower() in ["right", "right door", "go through right door"]:
            baseM.showText(player, "You start towards the right door when suddenly, your body moves toward the left door. [continue]",screen)
            baseM.showText(player, "You struggle to take control but it is too late. [continue]",screen)
            baseM.showText(player, "You enter the left door which reveals a statue with red glowing eyes. [continue]",screen)
            baseM.showText(player, "Suddenly the statue begins to move",screen)
            baseM.runBasicFight(screen, player, [Gargoyle()])
            break
        elif choice.lower() in ["leave"]:
            baseM.showText(player, "As you leave the room, your headache disappears. [continue]",screen)
            break
        else:
            baseM.checkCommands(choice, player,screen)
    return player
    




























