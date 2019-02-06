import sys
import random, console, pScript, Mtesting
from pScript import PChar

#Functions
def ClimbFloorEffects(player):
    #Effects on floor climb
    if "Corrupt Blood" in player.items:
        player.health += 10

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
    elif Input.title() in ["Continue", "C", "Cont"]:
        x = 1
        #add continue to next room
    else:
        print("This is not one of your options...")

def initIntro(player):
    input("You see a large grey structure looming in the distance.. [Approach]") #This is the intro.. Needs work...
    input("As you approach, a giant stone door slowly rises, revealing a dark room, faintly lit by the setting Sun outside... [Continue]")
    input("You see a note laying atop a pile of frayed cloth armor and a rusty sword.. [Read note]")
    input("The door slams shut behind you! Deep in the dungeon you see a dim light... [Approach]")
    choice = input("You take the torch, wondering what lies within the dungeon... [Return to Note, Continue into Dungeon]")
    while True:
        if choice.title() in ["Return", "R", "Return To Note", "Note"]:
            input("You walk back to the note, taking it along with the armor and the sword.. [Continue]")
            player.items.append(firstLetter())
            print("The First Letter was added to your inventory! Use [Inventory] to read it")
            player.items.append(rustySword())
            print("Rusty Sword was added to your inventory! You're going to need it...")
            player.items.append(frayedCloth())
            print("Frayed Cloth was added to your inventory!")
            break
        elif choice.title() in ["Continue", "C", "Continue Into Dungeon", "Dungeon"]:
            input("You continue walking into the dungeon and begin to feel very cold...[Continue]")
            player.health -= 3
            print("You regret not taking the cloth and sword.")
            break
        checkCommands(choice, player)
        choice = input("Continue into the dungeon or return to read the note?")
    return player

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
        if "Tester Sword" in player.items:
            dmg += 1000
        if "Heavy Sword" in player.items:
            dmg += 35
        if "Rusty Knife" in player.items:
            dmg += 1
        for i in player.items:
            try:
                dmg = i.boostDamage(dmg)
            except AttributeError:
                dmg = dmg
        return dmg
    elif Type == "def":
        dfns = 1
        if "Shield" in player.items:
            dfns += 10
        return dfns

def playerInputFight(player, enemies, defense = 0):
    #Asks for player input during fights (whether they should attack or defend). Returns the amount of block they gain from that turn.
    #You should not need to use this function if you're making a basic fighting room.
    turn = input("What do you do? [Attack, Defend, Magic]\n")
    if turn.title() in ["Attack", "A", "Atk"]:
        en, j = getFirstAliveEnemy(enemies)
        dmg = modifyPlayerEffects('atk', player)
        print("You attack {} {}, dealing {} damage".format(en.type, j+1, dmg))
        en.health -= dmg
        if en.health <= 0:
            en.death(player)
            enemies[j] = None
        return defense
    elif turn.title() in ["Defend", "D", "Def", "Dfnd"]:
        defense += modifyPlayerEffects('def', player)
        print("You defend yourself, blocking against {} damage".format(defense))
        return defense
    elif turn.title() in ["Magic", "M", "Mgc", "Alakazam"]:
        magiclist=[]
        truemagiclist=[]
        for n in player.items:
            if issubclass(n,magicItem):
                magiclist.append(n.name)
                truemagiclist.append(n)
        print (*magiclist, sep=" ")
        if magiclist is not None:
            magicchoice = input("Which magic item would you like to use? \n")
            if magicchoice in magiclist:
                try:
                    magicidentifier = magiclist.index(magicchoice)
                    truemagiclist[magicidentifier].magic()
                except AttributeError:
                    print("Oops! That is not a magic item")
        return defense
    else:
        checkCommands(turn, player)
        return playerInputFight(player, enemies, defense)

def runBasicFight(player, enemies, pBlock = 0):
    #Runs a basic fight with a given player and list of enemies. Enemies should be a class which extends basicEnemy
    #DO NOT INCLUDE A VALUE FOR pBlock! THIS IS SET WHEN THE CODE IS RUNNING.
    for i in range(len(enemies)):
        if i is not None:
            atk, dmg = enemies[i].move()
            print("{} {} uses {}, dealing {} damage.".format(enemies[i].type, i+1, atk, dmg))
            if pBlock > 0:
                pBlock -= dmg
                if pBlock < 0:
                    player.health += pBlock
                    pBlock = 0
                    print("You blocked {} damage.".format(pBlock))
                elif pBlock >= 0:
                    print("You blocked {} damage.".format(dmg))
            else:
                player.health -= dmg
            if atk == "Rob":
                robbed = random.randint(3,6)
                print("The {} stole {} of your gold!".format(enemies[i].type, robbed))
                player.gold -= robbed
                enemies[i].loot.append(("Gold",robbed))
            elif atk == "Siphon":
                print("The {} siphons {} of your hp!".format(enemies[i].type, dmg))
                enemies[i].health += dmg
                if enemies[i].health > enemies[i].maxHp:
                    enemies[i].health = enemies[i].maxHp
            elif atk == "Block":
                defense = enemies[i].baseDef
                print("The {} blocks for {} damage".format(enemies[i].type, defense))
        checkPlayer(player)
    pBlock = playerInputFight(player, enemies, pBlock)
    if getFirstAliveEnemy(enemies) is not None and player.alive:
        print("Your HP: {}\t\tEnemy's HP: {}".format(player.health, getFirstAliveEnemy(enemies)[0].health))
        runBasicFight(player, enemies, pBlock)
    elif not player.alive:
        return player
    else:
        choice = input("You defeated the enemies! [Continue]")
        checkCommands(choice, player)
        return player

def constructPlayer(data):
    #Constructs a player class based on data given in the following format.
    # health / gold / item1,item2,item3
    p = PChar()
    datal = data.split(' / ')
    p.health = int(datal[0])
    p.gold = int(datal[1])
    p.items = datal[2].split(",")
    for i in p.items:
        if i == '':
            p.items.remove(i)
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
        self.health = 10
        self.maxHp = 10
        self.loot = []
        self.options = {}

    def death(self, player):
        player.gold += random.randint(20, 40)
        for i in self.loot:
            if i[0] == "Gold":
                player.gold += i[1]
            else:
                player.items.append(i)

    def move(self):
        atk = random.choice(list(self.options.keys()))
        return atk, (self.baseDamage + self.options[atk])

class Zomboman(basicEnemy):
    def __init__(self):
        self.type = "Zombo-man"
        self.baseDamage = 1
        self.baseDef = 1
        self.health = 10
        self.maxHp = 10
        self.loot = [("Gold",random.randint(5,10))]
        self.options = {"Punch":0, "Block":-1}
        
class Ghoul(basicEnemy):
    #Represents a basic Ghoul
    def __init__(self):
        self.type = "Ghoul"
        self.baseDamage = 7
        self.health = 40
        self.maxHp = 40
        self.loot = [("Gold",random.randint(10,20)),random.choice(["Ghoul Claw"])]
        self.options = {"Swipe":0,"Rob":-2,"Siphon":-3} #These numbers determine how much damage the attack deals based on baseDamage. ex. Siphon deals 7-3=4 damage.
    
class ShivMan(basicEnemy):
    def __init__(self):
        self.type = "Assassin"
        self.baseDamage = 10
        self.health = 70
        self.maxHp = 70
        self.loot = [("Gold",random.randint(70,130), "Shiv")]
        self.options = {"Stab":0,"Rob":-2,"Slash":+2}

#Items
class basicItem():
    def __init__(self):
        self.name = None
        self.desc = ""

    def __str__(self):
        return self.name

    def readDesc(self):
        print(self.desc)

class firstLetter(basicItem):
    def __init__(self):
        self.name = "Letter From the Deceased"
        self.desc = """The letter is tattered and some words are missing.
The faded words read:
Deare
If th   lett r  as rea hed you  I  m pr bably de d.
[]
 ov
"""

class magicItem(basicItem):
    # Magic Items should have a function to replace donothing in self.magic. This function will run whenever a player chooses the magic option in a fight
    def donothing():
        print("")
    def __init__(self):
        self.name = "Magic Item"
        self.desc = "Abracadabra! Use this item in combat for special abilities"
        self.magic = donothing()
class corruptBlood(basicItem):
    def __init__(self):
        self.name = "Corrupt Blood"
        self.desc = "A strange bluish-purple liquid..."

    def onFloorClimb(self, player):
        player.health += 10

class basicSword(basicItem):
    def __init__(self):
        self.name = "Sword"
        self.desc = "A weapon, I think."
        self.damage = 10

    def boostDamage(self, initial):
        return initial+self.damage

class rustySword(basicSword):
    def __init__(self):
        self.name = "Rusty Sword"
        self.desc = "A rusted, britle sword from a traveler long forgotten..."
        self.damage = 4

class shiv(basicSword):
    def __init__(self):
        self.name = "Shiv"
        self.desc = "Stabby stabby!"
        self.damage = 7

class basicDefensiveItem(basicItem):
    def __init__(self):
        self.name = "Shield"
        self.desc = "Use it"
        self.block = 10

class frayedCloth(basicDefensiveItem):
    def __init__(self):
        self.name = "Frayed Cloth Armor"
        self.desc = "A frayed, deteriorating cloth..."
        self.block = 4
