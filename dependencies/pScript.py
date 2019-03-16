import random
from itemStats import loincloth

class PChar(): #intializes the class. The Main handles this, so you don't need it in your room.
    def __init__(self):
        self.health = 100
        self.gold = random.randint(101,149)
        self.items = [loincloth()]
        self.alive = True
        self.damage = 3
        self.block = 3
        self.maxHp = 100
        self.curses = []
        #These are non-main attributes of the player.
        self.timeClimbing = 0
        self.impossible = False

#I'd recommend having these as methods inside the player class so they're easier to use.
def checkDeath(Player): #checks if the player is dead. Handled automatically in the damage() function.
    if Player.health <= 0:
        death(Player)

def death(Player): # sets Player.alive to False. Handled automatically by the checkDeath() function.
#Note: your level should have a way to end if the player dies (if Player.alive == False) whenever the player takes damage.
    Player.alive = False

#def checkDebt(Player): **OBSOLETE FUNCTION**
 #   if Player.gold <= 0:
  #      
   #     baseM.showText("You are in debt! The IRS has come to extort money out of you.",screen) 
    #    baseM.showText("you lose all your items and " + -Player.gold + " health.",screen)
     #   if "loincloth" in Player.items:
      #      baseM.showText("they even take your Loincloth! -1 to public decency",screen) 
       # Player.health -= char.gold
        #Player.items = []
        #Player.gold = 0

def heal(Player, HP): # a heal function. HP should be an integer.
    Player.health += HP
    if Player.health > Player.maxHp:
        Player.health = Player.maxHp
    baseM.showText("you healed " + str(HP,screen) + " health",screen)
    if Player.alive == True:
        baseM.showText("Current health: " + str(Player.health,screen),screen),screen)

def damage(Player, HP): # a damage function. HP should be an integer.
    Player.health -= HP
    baseM.showText("you took " + str(HP,screen) + " damage",screen)
    checkDeath(Player)
    if Player.alive == True:
        baseM.showText("Current health: " + str(Player.health,screen),screen),screen)
    

def spendGold(Player, cost): # A function for the player losing money. Returns False if the player doesn't have enough money to spend. ("cost" should be an integer.)
    if Player.gold < cost:
        baseM.showText("you don't have enough money",screen)
        return False
    else:
        Player.gold -= cost
        baseM.showText("you lose " + str(cost,screen) + " gold",screen)
        baseM.showText("Current gold: " + str(Player.gold,screen),screen),screen)
        return True

def earnGold(Player, gold): # A function for the player gaining money. ("gold" should be an integer.)
    Player.gold += gold
    baseM.showText("you gain " + str(gold,screen) + " gold",screen)
    baseM.showText("Current gold: " + str(Player.gold,screen),screen),screen)


def addItem(Player, item): #adds an item to the list of items
    Player.items.append(item)
    baseM.showText("the " + item.name + " was added to your inventory",screen)


def removeItem(Player, item): #adds an item to the list of items. Returns False if the item doesn't exist in the inventory.
    if item in Player.items:
        Player.items.remove(item)
        baseM.showText("you lost the " + item.name,screen)
        if item == "loincloth":
            baseM.showText("you lost your loincloth! -1 to public decency!",screen)
        return True
    else:
        baseM.showText("You don't have the " + item.name,screen)
        return False
        



#def update(Player):  **OBSOLETE FUNCTION**
    #checkDeath(Player)
    #checkDebt(Player)





