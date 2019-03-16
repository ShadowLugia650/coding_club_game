import sys
sys.path.insert(0, 'dependencies')
import baseM

class Junior(baseM.basicEnemy):
    def __init__ (self):
        self.type="Treasure goblin"
        self.maxHp=1
        self.health=1
        self.baseDamage=25
        self.baseDef = 0
        self.block = 0
        self.options = {"Stab":0}
        self.loot=[("Gold",80)]
        
        
def run (player, screen):
    baseM.showText("A snarling, scrawny goblin leaps out of the darkness!")
    baseM.runBasicFight(player, [Junior()], playerFirst=True)
    return player


