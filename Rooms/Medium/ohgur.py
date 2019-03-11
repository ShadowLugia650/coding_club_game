import sys
sys.path.insert(0, 'dependencies')
import baseM, itemStats

class Senior(baseM.basicEnemy):
    def __init__ (self):
        self.type="Ohgur"
        self.baseDamage=3
        self.baseDef=2
        self.block = 0
        self.maxHp=70
        self.health=70
        self.options = {"Kick":7, "Slash":12}
        self.loot=[itemStats.ohgurGuts(), itemStats.ohgurGuts()]
        
        
def run (player):
    print("A raging, drooling Ohgur charges at you!")
    baseM.runBasicFight(player, [Senior()],0,True)
    return player
