import sys
import random, console, pScript, Mtesting
from pScript import PChar
import itemStats
from itemStats import *
from curseScript import *

#Functions
def checkPlayer(player):
    #Checks if the player is dead.
    if player.health <= 0:
        player.alive = False

def checkCommands(Input, player):
    #Checks for game-wide commands, such as help, status, inventory, and tester commands.
    if Input != '' and Input[0] == '`':
        Mtesting.specials(Input, player)
    if Input.title() in ["Help", "?"]:
        console.playerhelp()
    elif Input.title() in ["Status", "Stat", "Me"]:
        console.status(player)
    elif Input.title() in ["Inventory", "Inv", "Items", "Bag"]:
        console.inventory(player)
    elif Input.title().split(" ")[0] in ["Inspect", "View", "Description", "Desc"]:
        keyword = Input.title().split(" ")[0]
        s = Input.title().split(keyword+" ")[1]
        try:
            itm = eval(strToClsNm(s))()
            if hasItem(itm, player):
                itm.readDesc()
            else:
                print("You don't have this item..")
        except NameError:
            print("This item doesn't seem to exist...")
    elif Input.title().split(" ")[0] in ["Drink", "Potion"]:
        keyword = Input.title().split(" ")[0]
        s = Input.title().split(keyword+" ")[1]
        try:
            itm = eval(strToClsNm(s))()
            if hasItem(itm, player):
                if issubclass(type(itm), basicPotion):
                    im = getItem(itm.name, player)
                    im.drinkPotion(player)
                    player.items.remove(im)
                else:
                    print("That item doesn't seem too drinkable to me...")
            else:
                print("You don't have this item..")
        except NameError:
            print("This item doesn't seem to exist...")
    else:
        print("This is not one of your options...")

def initIntro(player):
    print("""Welcome to the Coding Club dungeon crawler game!
************************************************
             Press any key to begin""")
    console.playerhelp()
    input()
    sys.path.insert(0, 'Rooms/Intros')
    import originalIntroM
    intros = [originalIntroM]
    intro = random.choice(intros)
    intro.run(player)
        
def getFirstAliveEnemy(enemies):
    #Finds the first enemy in the given list that is not None. If all are None, returns None
    #You should not need to use this function if you're making a basic fighting room.
    for i in enemies:
        if i is not None:
            return i, enemies.index(i)
    return None

def modifyPlayerEffects(Type, player):
    #Modifies the player's damage/defense when using attack or block in battle, based on their items.
    #You should not need to use this function if you're making a basic fighting room.
    if Type == "atk":
        dmg = 1
        for i in player.items:
            if issubclass(type(i), basicSword):
                dmg = i.boostDamage(dmg)
        return dmg
    elif Type == "def":
        dfns = 1
        for i in player.items:
            if issubclass(type(i), basicDefensiveItem):
                dfns = i.boostDefense(dfns)
        return dfns

def playerInputFight(player, enemies, defense = 0):
    #Asks for player input during fights (whether they should attack or defend). Returns the amount of block they gain from that turn.
    #You should not need to use this function if you're making a basic fighting room.
    curseEfx = {}
    for curse in player.curses:
        if type(curse) == exhaustion:
            efx = curse.onCombatTurn(player)
            curseEfx["Exhaustion"] = efx
    turn = input("What do you do? [Attack, Defend, Magic]\n")
    if turn.title() in ["Attack", "A", "Atk"]:
        en, j = getFirstAliveEnemy(enemies)
        dmg = modifyPlayerEffects('atk', player)
        if "Exhaustion" in curseEfx.keys() and curseEfx["Exhaustion"][1] == "Damage":
            dmg -= curseEfx["Exhaustion"][0]
        print("You attack {} {}, dealing {} damage".format(en.type, j+1, dmg))
        en.takeDamage(dmg, player)
        for item in player.items:
            try:
                player.health += item.lifesteal
                if player.health > player.maxHp:
                    player.health = player.maxHp
            except AttributeError:
                pass
        if en.health <= 0:
            en.death(player)
            enemies[j] = None
        return defense
    elif turn.title() in ["Defend", "D", "Def", "Dfnd"]:
        defense += modifyPlayerEffects('def', player)
        if "Exhaustion" in curseEfx.keys() and curseEfx["Exhaustion"][1] == "Block":
            defense -= curseEfx["Exhaustion"][0]
        print("You brace yourself, defending against {} damage.".format(defense))
        return defense
    elif turn.title() in ["Magic", "M", "Mgc", "Alakazam"]:
        en, j = getFirstAliveEnemy(enemies)
        magiclist=[]
        truemagiclist=[]
        for n in player.items:
            if issubclass(type(n),basicMagicItem):
                magiclist.append(n.name.lower())
                truemagiclist.append(n)
        print (*magiclist, sep=" \n")
        if magiclist != []:
            while True:
                magicchoice = input("Which magic item would you like to use? \n")
                if magicchoice.lower() in magiclist:
                        magicidentifier = magiclist.index(magicchoice)
                        truemagiclist[magicidentifier].magic(self, player, en)
                        return defense
        else:
            print("Sorry! You do not have any magic items")
        return defense
    else:
        checkCommands(turn, player)
        return playerInputFight(player, enemies, defense)

def runBasicFight(player, enemies, pBlock = 0, playerFirst = False, turn = 0):
    #Runs a basic fight with a given player and list of enemies. Enemies should be a class which extends basicEnemy
    #DO NOT INCLUDE A VALUE FOR pBlock! THIS IS SET WHEN THE CODE IS RUNNING.
    if turn == 0:
        for i in player.items:
            if i.name == "Demonic Sword":
                i.damage = 10
    if not playerFirst:
        for i in range(len(enemies)):
            if enemies[i] is not None:
                atk, dmg = enemies[i].move(player)
                #Special Enemy Stuff lol
                if atk == "Future Doom Damage":
                    print("{} {}'s Future Doom comes true! You take {} damage.".format(enemies[i].type, i+1, dmg))
                    atk, dmg = enemies[i].move()
                elif "Summon: " in atk:
                    enemies.append(dmg)
                elif atk == "Flee":
                    print("The {} fled the combat!".format(enemies[i].type))
                    return player
                #Ok end of Special Enemy stuff now
                print("{} {} uses {}, dealing {} damage.".format(enemies[i].type, i+1, atk, dmg))
                if pBlock > 0:
                    for j in player.items:
                        if issubclass(type(j), basicDefensiveItem):
                            dmg = j.whenAttacked(dmg, enemies[i])
                if dmg > 0:
                    if dmg > pBlock:
                        dmg -= pBlock
                        player.health -= dmg
                    else:
                        pBlock -= dmg
                if atk == "Rob":
                    robbed = random.randint(3,6)
                    print("The {} stole {} of your gold!".format(enemies[i].type, robbed))
                    player.gold -= robbed
                    #enemies[i].loot.append(("Gold",robbed))
                elif atk == "Siphon":
                    if dmg > 0:
                        print("The {} siphons {} of your hp!".format(enemies[i].type, dmg))
                        enemies[i].health += dmg
                        if enemies[i].health > enemies[i].maxHp:
                            enemies[i].health = enemies[i].maxHp
                elif atk == "Block":
                    enemies[i].block += enemies[i].baseDef
                    print("The {} blocks for {} damage".format(enemies[i].type, enemies[i].block))
            checkPlayer(player)
            if not player.alive:
                return player
    pBlock = playerInputFight(player, enemies, pBlock)
    if getFirstAliveEnemy(enemies) is not None and player.alive:
        print("Your HP: {}\t\tEnemy's HP: {}".format(player.health, getFirstAliveEnemy(enemies)[0].health))
        return runBasicFight(player, enemies, pBlock, False, turn+1)
    elif not player.alive:
        return player
    else:
        choice = input("You defeated the enemies! [Continue]")
        checkCommands(choice, player)
        return player

def getItem(name, player):
    for i in player.items:
        if i.name == name:
            return i
    return None
    
def hasItem(itemClass, player):
    for i in player.items:
        if i.name == itemClass.name:
            return True
    return False
    
def hasWeapon(player):
    for i in player.items:
        if issubclass(type(i), basicSword):
            return True
    return False
    
def hasBlock(player):
    for i in player.items:
        if issubclass(type(i), basicDefensiveItem):
            return True
    return False

def hasMagic(player):
    for i in player.items:
        if issubclass(type(i), basicMagicItem):
            return True
    return False
    
def strToClsNm(string):
    sl = string.split(" ")
    cn = sl[0].lower()
    for i in range(len(sl)-1):
        cn += sl[i+1].title()
        cn = cn.replace("'","")
    return cn
    
def calculateFinalScore(player, floorsClimbed):
    score = 0
    score += player.gold
    for i in player.items:
        try:
            score += i.value
        except AttributeError:
            pass
    score += 100*floorsClimbed #modify to change based on type of floors
    return score
    
def constructPlayer(data):
    #Constructs a player class based on data given in the following format.
    # health / gold / item1,item2,item3
    p = PChar()
    datal = data.split(' / ')
    p.health = int(datal[0])
    p.gold = int(datal[1])
    p.items = []
    itms = datal[2].split(",")
    for i in itms:
        if i != '':
            p.items.append(eval(strToClsNm(i))())
    return p
    
def packagePlayer(player):
    #Packages a player class into the format given above.
    d = '{} / {} / '.format(player.health, player.gold)
    for i in player.items:
        d += "{},".format(i)
    return d+'\n'

def readStoredPlayers(file):
    #Reads players stored in the format above in the given file
    txt = open(file,'r')
    if txt.mode == 'r':
        doc = txt.read()
    ps = []
    for i in doc.split('\n'):
        if i != '':
            ps.append(constructPlayer(i))
    return ps

def writePlayer(player, file):
    #Packages and writes a given player into the provided file
    #Automatically accounts for players already in the file.
    players = readStoredPlayers(file)
    txt = open(file,'w+')
    players.append(player)
    for i in players:
        t = packagePlayer(i)
    txt.write(t)
    

#Enemies!
class basicEnemy():
    #A class which represents any given enemy. Can be extended to a specific type
    def __init__(self):
        self.type = None #This should be a string which represents your enemy.
        self.baseDamage = 0
        self.baseDef = 0
        self.block = 0
        self.health = 10
        self.maxHp = 10
        self.loot = []
        self.options = {}

    def takeDamage(self, damage, player):
        dmg = damage - self.block
        if dmg > 0:
            self.health -= damage
        
    def death(self, player):
        for i in self.loot:
            if type(i) == tuple and i[0] == "Gold":
                player.gold += i[1]
            else:
                player.items.append(i)

    def move(self, player = None):
        self.block = 0
        atk = random.choice(list(self.options.keys()))
        return atk, (self.baseDamage + self.options[atk])
    
class twoPhaseEnemy(basicEnemy):
    def __init__(self):
        self.type = None
        self.baseDamage = 0
        self.baseDef = 0
        self.block = 0
        self.health = 100
        self.maxHp = 100
        self.loot = []
        self.options = {}
        self.optionsP2 = {}
        self.phase = 1
        self.condition = (health <= round(maxHp/2))
        
    def move(self):
        self.block = 0
        if self.phase == 1:
            if self.condition:
                self.phase = 2
            atk = random.choice(list(self.options.keys()))
            return atk, (self.baseDamage + self.options[atk])
        elif self.phase == 2:
            atk = random.choice(list(self.optionsP2.keys()))
            return atk, (self.baseDamage + self.optionsP2[atk])
    
class Zomboman(basicEnemy):
    def __init__(self):
        self.type = "Zombo-man"
        self.baseDamage = 1
        self.baseDef = 1
        self.block = 0
        self.health = 10
        self.maxHp = 10
        self.loot = [("Gold", 6), zombomanGuts()]
        self.options = {"Punch":0, "Block":-1}
        
class Ghoul(basicEnemy):
    #Represents a basic Ghoul
    def __init__(self):
        self.type = "Ghoul"
        self.baseDamage = 7
        self.baseDef = 0
        self.block = 0
        self.health = 40
        self.maxHp = 40
        self.loot = [("Gold", 14),random.choice([ghoulClaw()])]
        self.options = {"Swipe":0,"Rob":-2,"Siphon":-3} #These numbers determine how much damage the attack deals based on baseDamage. ex. Siphon deals 7-3=4 damage.
    
class ShivMan(basicEnemy):
    def __init__(self):
        self.type = "Assassin"
        self.baseDamage = 10
        self.baseDef = 0
        self.block = 0
        self.health = 70
        self.maxHp = 70
        self.loot = [("Gold", 42, shiv())]
        self.options = {"Stab":0,"Rob":-2,"Slash":+2}
