import sys
sys.path.insert(0, 'dependencies')
import baseM

class Junior(baseM.basicEnemy):
    def __init__ (self):
        self.type="Treasure goblin"
        self.maxHp=1
        self.health=1
        self.baseDamage=20
        self.loot=[["Gold",200]]
        
        
def run (player):
    print("A snarling, scrawny goblin leaps out of the darkness!")
    baseM.runBasicFight(player, [Junior()],0,True)
    return player
