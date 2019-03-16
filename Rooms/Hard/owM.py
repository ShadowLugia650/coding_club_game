import sys, random

sys.path.insert(0, 'dependencies')
import baseM, itemStats

class Heart(baseM.basicEnemy):
    def __init__(self):
        self.type = "Heart"
        self.health = 550
        self.maxHp = 550
        self.baseDamage = 2
        self.baseDef = 0
        self.block = 0
        self.damageDealt = 0
        self.loot = [("Gold", 172),itemStats.corruptBlood()]
        self.options = {"Siphon":18, "Pummel":0, "Reap":0}
        self.lastAttack = None
        self.turnNum = 0
        self.pummelHits = 0
        
    def move(self, player):
        self.turnNum += 1
        if self.turnNum % 3 == 0:
            atk = "Reap"
            self.baseDamage += 5*self.turnNum/3
            self.lastAttack = None
            return atk, 0
        else:
            if self.lastAttack is None:
                atk = random.choice(["Pummel", "Siphon"])
            else:
                if self.lastAttack == "Siphon":
                    atk = "Pummel"
                elif self.lastAttack == "Pummel":
                    atk = "Siphon"
            if atk == "Pummel":
                self.pummelHits += 5
                self.lastAttack = atk
                return "{} ({}x{})".format(atk, (self.options[atk]+self.baseDamage), self.pummelHits), ((self.options[atk]+self.baseDamage)*self.pummelHits)
            elif atk == "Siphon":
                self.lastAttack = atk
                return atk, self.options[atk]+self.baseDamage

def ignore(player, screen):
    baseM.showText("You walk past the heart to the door at the end of the room.")
    choice = baseM.showText("The door slams shut! Next to it lies a slip of paper in a crack in the wall..[Take Paper, Leave it]")
    if choice.title() in ["Take", "T", "Paper", "P", "Take Paper"]:
        baseM.showText("As you grab the paper, the heart begins draining your life. ")
        baseM.showText("You take the paper, and the door opens slowly")
        baseM.showText("As soon as the door opens you hurry through and escape to the next room while the heart remains trapped in its own.")
        baseM.showText("You take 20 damage.")
        player.health -= 20
        baseM.checkPlayer(player, screen)
    elif choice.title() in ["Leave", "L", "Leave It"]:
        baseM.showText("The heart moves toward you and you feel the life start to slowly drain from your body.")
        for i in player.items:
            try:
                if issubclass(type(i), itemStats.basicSword):
                    baseM.showText("You attack the door with your weapons, ultimately destroying it.")
                    player.health -= 30
                    baseM.showText("You take 30 damage.")
                    baseM.checkPlayer(player, screen)
                    return
            except TypeError:
                pass
        baseM.showText("You cannot open the door, and the heart fully drains your life.")
        player.health = 0
        player.alive = False
    else:
        baseM.checkCommands(choice, player)
        ignore(player, screen)

def run(player, screen):
    # runs the room
    baseM.showText("You enter a room and see a bluish-purple heart floating in the middle...")
    choice = baseM.showText("What do you do? [Attack, Ignore, Run]\n")
    if choice.title() in ["Attack", "A", "Atk"]:
        baseM.showText("You prepare to attack the heart. It bleeds but is ultimately unharmed.")
        baseM.showText("The heart suddenly attacks you back! You try to defend but your best efforts seem in vain...")
        baseM.runBasicFight(player, [Heart()])
        if player.alive:
            baseM.showText("As the heart falls, you notice a bluish-purple liquid in your bag. [Continue]")
    elif choice.title() in ["Ignore", "I"]:
        ignore(player, screen)
    elif choice.title() in ["Run", "R"]:
        baseM.showText("You flee the room as fast as your legs can take you. Looking back, you see the heart slowly moving toward you...")
        baseM.showText("The heart starts to drain your health and your consciousness starts to fade....[Continue]")
        baseM.showText("Suddenly, you see an open doorway above you! You grab the ledge and pull yourself out of the room gravely injured, but ultimately alive.")
        dmg = player.health -1
        player.health = 1
        sel = baseM.showText("You take {} damage as you escape...[Continue]".format(dmg))
    else:
        baseM.checkCommands(choice, player)
        run(player, screen)
    return player




