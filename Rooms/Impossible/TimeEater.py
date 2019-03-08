import sys, random, time, math
sys.path.insert(0, 'dependencies')
import baseM, itemStats

class timeEater(baseM.basicEnemy):
    def __init__(self):
        self.type = "Time Eater"
        self.baseDamage = 10
        self.health = 450
        self.maxHp = 450
        self.loot = [("Gold", random.randint(130,170))], itemStats.hungryClock()]
        self.options = {"Consume":0, "Strike":0, "Future Doom":30, "Stall":0}
        self.optionsP2 = {"Minute Spear":"self.baseDamage+5", "Hour Skewer":"self.baseDamage*2", "Future Doom":"self.baseDamage*5"}
        self.phase = 1
        self.turnCounter = 0
        self.timedTurn = (0, 0)
        
    def move(self, player):
        self.turnCounter += 1
        print("Take your time...")
        if self.phase == 1:
            if self.timedTurn[0] == (self.turnCounter - 3):
                return "Future Doom Damage", self.timedTurn[1]
            atk = random.choice(list(self.options.keys()))
            if atk == "Consume":
                self.health += self.baseDamage
                if self.health > self.maxHp:
                    self.health = self.maxHp
                dmg = 0
            elif atk == "Future Doom":
                self.timedTurn = (self.turnCounter, self.options[atk]+self.baseDamage)
                dmg = 0
            elif atk == "Stall":
                for i in range(5):
                    time.sleep(2)
                    print('.',end='')
                self.baseDamage *= 10
                dmg = 0
            else:
                dmg = self.options[atk]+self.baseDamage
            if self.health <= self.maxHp/2:
                self.phase = 2
        elif self.phase == 2:
            atk = random.choice(list(self.optionsP2.keys()))
            hit = True
            if self.timedTurn[0] == (self.turnCounter - 2):
                return "Future Doom Damage", self.timedTurn[1]
            if atk == "Hour Skewer":
                hit = random.randint(1,100)<75
            elif atk == "Future Doom":
                self.timedTurn = (self.turnCounter, eval(self.optionsP2[atk]))
                dmg = 0
            if hit:
                dmg = eval(self.optionsP2[atk])
            else:
                dmg = 0
                print()
        return atk, dmg

def run(player):
    t = timeEater()
    if len(player.items) > 50:
        t.baseDamage = math.ceil(len(player.items)/3)
    t.baseDamage *= player.timeClimbing
    print("You walk into a large spacious room. There are clocks all over the walls, each with a different name on it.")
    print("As you continue walking you see your name. Suddenly, the clock starts to grow, and the hands reach out toward you.")
    baseM.runBasicFight(player, [t])
    return player
