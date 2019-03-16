import sys
sys.path.insert(0, 'dependencies')
import baseM, random, itemStats

def run(player, screen):
    baseM.showText("A golden idol stands in the middle of the hallway",screen)
    baseM.showText("Hack pieces off or touch the idol?",screen)
    choice = baseM.showText("[hack pieces, touch idol]",screen)
    thisIdol = Idol()
    while True:
        if choice.lower() in ["hack pieces","hack", "h"]:
            baseM.runBasicFight(player, [thisIdol], 0, True, 5)
            baseM.showText("You broke "+str(round((1000-thisIdol.health(,screen),screen)/2,screen),screen)+" worth of gold fragments off the idol!",screen),screen)
            player.gold+=round((1000-thisIdol.health())/2)
            return player
        elif choice.lower() in ["touch idol","touch", "t"]:
            baseM.showText("The idol shrinks in size until it can fit in your backpack",screen)
            player.items.append(itemStats.idol())
            return player
        else:
            baseM.checkCommands(choice, player)

class Idol(baseM.basicEnemy):
    def __init__ (self):
        self.type="Idol"
        self.maxHp=1000
        self.health=1000
        self.baseDamage=0
        self.baseDef = 0
        self.block = 0
        self.options = {"Glow":0}
        self.loot=[itemStats.idolShield()]
        





