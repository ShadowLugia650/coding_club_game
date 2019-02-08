import random, sys
sys.path.insert(0, 'dependencies')
import console, pScript, baseM
from itemStats import peasantsBlade,kingsBlade,herosBlade
class Collector(baseM.basicEnemy):
    def __init__(self):
        self.type = "Collector"
        self.baseDamage = 1
        self.health = 100
        self.maxHp = 100
        self.loot = [("Gold",random.randint(80,120))]
        self.options = {"Stab":0,"Siphon":-3,"Slash":+1}
def run(player):
    x=Collector()
    print ("""Opening the door, you peer cautiously into the room.
A hooded figure with three swords strapped to his back stands at its center.

""")
    while True:
        response0 = console.getInput(player, ["1"], "Press 1 to continue")
        if response0.lower() == "1":
            break
    print (""" The head swivels smoothly toward you, and a hollow voice says,

"Choose your death, or choose your glory
Blood and steel will write your story
If you fear a gruesome end
My farmer's blade will give and bend
Should you desire jewels and gold
My blade of kings is yours to hold
But if you fear not war or strife
My hero's blade will take your life

Choose wisely, adventurer. The blade I wield will be your reward should you best me."
Press 1 to choose the peasant's blade
Press 2 to choose the king's blade
Press 3 to choose the hero's blade (don't do it)
""")
    for objects in player.items:
        x.baseDamage+=2
        x.health+=30
        x.maxHp+=30
    enemylist=[x]
    while True:
        response = console.getInput(player, ["1", "2","3"], "Make your choice")
        if response.lower() == "1":
            x.baseDamage+=2
            x.loot=[("Gold",random.randint(100,120)),peasantsBlade()]
            baseM.runBasicFight(player, enemylist)   
            return player
        if response.lower() == "2":
            x.baseDamage+=8
            x.loot=[("Gold",random.randint(250,300)),kingsBlade()]
            baseM.runBasicFight(player, enemylist)
            return player
        if response.lower() =="3":
            x.baseDamage+=30
            x.loot=[("Gold",random.randint(120,150)),herosBlade()]
            baseM.runBasicFight(player, enemylist)
            return player



