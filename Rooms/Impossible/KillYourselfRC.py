import sys
sys.path.insert(0, 'dependencies')
import baseM
import itemStats
class Yourself(baseM.basicEnemy):
    def __init__(self):
        self.type = "Yourself"
        self.baseDamage = 0
        self.health = 200
        self.maxHp = 200
        self.loot=[itemStats.vileBlade()]
        self.options = {"Stab":-5,"Slash":+10}
def run(player):
    you=Yourself()
    you.baseDamage+=baseM.modifyPlayerEffects("atk", player)
    you.health=player.health*3
    you.maxHp=player.health*3
    baseM.runBasicFight(player, [you], 0, True)
    
