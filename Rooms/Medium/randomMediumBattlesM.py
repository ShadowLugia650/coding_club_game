import sys, random
sys.path.insert(0, 'dependencies')
import baseM, itemStats

class Grenlim(baseM.basicEnemy):
    def __init__(self):
        self.type = "Grenlim"
        self.baseDamage = 13
        self.baseDef = 1
        self.health = 35
        self.maxHp = 35
        self.loot = [("Gold", random.randint(30,50))]
        self.options = {"Slash":2, "Strike":0}

def run(player):
    enemies = [random.choice([Grenlim()])]
    print("You encountered a {}!".format(enemies[0].type))
    choice = input("What do you do? [Fight, Run]\n")
    if choice.title() in ["Fight", "F", "Attack"]:
        print("You engage the {} in combat!".format(enemies[0].type))
        baseM.runBasicFight(player, enemies)
    elif choice.title() in ["Flee", "Run", "R"]:
        print("You run away from the {} and it deals {} to you.".format(enemies[0].type, enemies[0].baseDamage))
        player.health -= enemies[0].baseDamage
    else:
        baseM.checkCommands(choice, player)
        run(player)
    return player
