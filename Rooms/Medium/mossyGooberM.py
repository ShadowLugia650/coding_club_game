import sys
sys.path.insert(0, 'dependencies')
import baseM, curseScript, itemStats

class MossyGoober(baseM.basicEnemy):
    def __init__(self):
        self.type = "Mossy Giant"
        self.health = 85
        self.baseDamage = 5
        self.options = {}
        self.loot = []

def run(player):
    print("You encounter a thicket of vines preventing you from proceeding. What do you do?")
    choice = input("[Push Through, Cut Vines, Go Back]")
    if choice.title() in ["Push", "Push Through", "Through", "P"]:
        print("You push through the vines to the other side. Unfortunately, you realize that the vines were actually poisonous.")
        tx = curseScript.toxins()
        tx.severity = 3
        player.curses.append(tx)
    elif choice.title() in ["Cut", "Vines", "Cut Vines", "C"]:
        if baseM.hasWeapon(player):
            print("As you carefully cut the vines you start to feel the ground move beneath you.")
        else:
            print("Without a proper weapon, you are unable to cut the vines.")
            run(player)
    elif choice.title() in ["Go Back", "Go", "Back", "G"]:
        print("You turn away from the vines only to find more vines blocking the entrance from which you came..")
        print("Or was it? As you look around, vines cover every wall and stretch in front of the many doorways into and out of this room.")
        print("Confused and dizzy, you sit down on the ground to reconsider your options.")
    else:
        baseM.checkCommands(choice,player)
        run(player)
    return player
