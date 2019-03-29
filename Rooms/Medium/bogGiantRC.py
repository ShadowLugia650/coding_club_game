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
    baseM.showText(player, """A gnarled tree trunk protrudes from the cracked tile of the floor.
Sticking from the top of the tree trunk is a sword of dark grey steel
How would you wish to proceed?
Press 1 to take the sword
Press 2 to leave""", screen)
    while True:
        choice=baseM.showText(player, "[Take the sword, Leave]",screen)
        if choice.lower() in ["1", "take", "sword", "take the sword"]:
            baseM.showText(player, """You yank hard on the sword, trying to dislodge it.
To your surprise, the floor begins to rumble and the tree trunk begins to rise.
You realize that the tree trunk is actually the head of a massive bog giant!""", screen)
            baseM.runBasicFight(screen, player, [BogGiant()], 0, True)
            return player
        elif choice.lower() in ["2", "leave", "l"]:
            baseM.showText(player, "You suspect a trap, so you leave the sword untouched.", screen)
            return player
        else:
            baseM.showText(player, "Sorry, that is not one of your options",screen)
        

























