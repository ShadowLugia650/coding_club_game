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
    print ("You enter a seemingly empty room. [continue]")
    print ("As you walk further in, you begin to feel dizzy.[continue]")
    print ("You see two doors at the end of the room.[continue]")
    print ("What do you do?")
    while True:
        choice = baseM.showText(player, "[Go through left door, Go through right door, Leave]",screen)
        if choice.lower() in ["left", "left door", "go through left door"]:
            print ("You start towards the left door when suddenly, your body moves toward the right door. [continue]")
            print ("You struggle to take control but it is too late. [continue]")
            print ("You enter the right door which reveals a golden goblet with a strange glowing liquid. [continue]")
            while True:
                print ("What do you do?")
                choice = input ("[Drink the liquid, Leave]")
                if choice.lower() in ["drink", "liquid", "drink the liquid"]:
                    print ("You drink the liquid and feel refreshed. You regain 30 health")
                    pScript.heal (player,30)
                    break
                elif choice.lower() in ["leave"]:
                    print ("You leave the room dumbfounded but unscathed")
                    break
                else:
                    baseM.checkCommands(choice, player,screen)
            break
        elif choice.lower() in ["right", "right door", "go through right door"]:
            print ("You start towards the right door when suddenly, your body moves toward the left door. [continue]")
            print ("You struggle to take control but it is too late. [continue]")
            print ("You enter the left door which reveals a statue with red glowing eyes. [continue]")
            print ("Suddenly the statue begins to move")
            baseM.runBasicFight(player, [Gargoyle()])
            break
        elif choice.lower() in ["leave"]:
            print ("As you leave the room, your headache disappears. [continue]")
            break
        else:
            baseM.checkCommands(choice, player,screen)
    return player
    
















