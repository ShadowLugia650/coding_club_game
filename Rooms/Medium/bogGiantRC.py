import baseM
import itemStats
import console
import curseScript
class BogGiant(baseM.basicEnemy):
    def __init__(self):
        self.type = "Bog Giant"
        self.baseDamage = 20
        self.baseDef = 0
        self.block = 0
        self.health = 200
        self.maxHp = 200
        self.loot=[itemStats.vileBlade()]
        self.options = {"Stab":-5,"Slash":+10}
def run(player, screen):
    baseM.showText("""A gnarled tree trunk protrudes from the cracked tile of the floor.
Sticking from the top of the tree trunk is a sword of dark grey steel
How would you wish to proceed?
Press 1 to take the sword
Press 2 to leave""")
    while True:
        choice=baseM.showText()
        if choice=="1":
            baseM.showText("""You yank hard on the sword, trying to dislodge it.
To your surprise, the floor begins to rumble and the tree trunk begins to rise.
You realize that the tree trunk is actually the head of a massive bog giant!""")
            baseM.runBasicFight(player, [BogGiant()], 0, True)
            return player
        elif choice=="2":
            print ("You suspect a trap, so you leave the sword untouched.")
            return player
        else:
            baseM.showText("Sorry, that is not one of your options")
        



