import sys, random
sys.path.insert(0, 'dependencies')
import baseM, itemStats
from curseScript import toxins

class Grenlim(baseM.basicEnemy):
    def __init__(self):
        self.type = "Grenlim"
        self.baseDamage = 13
        self.baseDef = 1
        self.health = 35
        self.maxHp = 35
        self.loot = [("Gold", random.randint(30,50))]
        self.options = {"Slash":2, "Strike":0}
        
class Snak(baseM.basicEnemy):
    def __init__(self):
        self.type = "Snak"
        self.baseDamage = 18
        self.health = 20
        self.maxHp = 20
        self.loot = [("Gold", random.randint(30,50))]
        self.options = {"Dry Strike":2, "Venomous Bite":-3}
        self.lastHit = "Dry Strike"
        
    def move(self, player):
        if self.lastHit == "Dry Strike":
            atk = random.choice(self.options.keys())
        else:
            atk = "Dry Strike"
        if atk == "Venomous Bite":
            v = toxins()
            v.severity = 3
            player.curses.append(v)
        self.lastHit = atk
        return atk, self.options[atk]+self.baseDamage
        
class Sorcerer(baseM.basicEnemy):
    def __init__(self):
        self.type = "Sorserr"
        self.baseDamage = 15
        self.health = 25
        self.maxHp = 25
        self.loot = [("Gold", random.randint(30,50)), itemStats.orbOfThunder()]
        self.options = {"Thunder Strike":3, "Siphon":-3}
        
def run(player):
    enemies = [random.choice([Grenlim(), Snak(), Sorcerer])]
    print("You encountered a {}!".format(enemies[0].type))
    choice = input("What do you do? [Fight, Run]\n")
    if choice.title() in ["Fight", "F", "Attack"]:
        print("You engage the {} in combat!".format(enemies[0].type))
        baseM.runBasicFight(player, enemies)
    elif choice.title() in ["Flee", "Run", "R"]:
        print("You run away from the {} and it deals {} to you.".format(enemies[0].type, enemies[0].baseDamage))
        if type(enemies[0]) == Snak:
            print("The Snak envenomated you with its attack!")
            player.curses.append(toxins())
        player.health -= enemies[0].baseDamage
    else:
        baseM.checkCommands(choice, player)
        run(player)
    return player
