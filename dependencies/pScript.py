import random, baseM
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
def checkDeath(player): #checks if the player is dead. Handled automatically in the damage() function.
    if player.health <= 0:
        death(player)

def death(player): # sets player.alive to False. Handled automatically by the checkDeath() function.
#Note: your level should have a way to end if the player dies (if player.alive == False) whenever the player takes damage.
    player.alive = False

#def checkDebt(player): **OBSOLETE FUNCTION**
 #   if player.gold <= 0:
  #      
   #     baseM.showText(player, "You are in debt! The IRS has come to extort money out of you.",screen) 
    #    baseM.showText(player, "you lose all your items and " + -player.gold + " health.",screen)
     #   if "loincloth" in player.items:
      #      baseM.showText(player, "they even take your Loincloth! -1 to public decency",screen) 
       # player.health -= char.gold
        #player.items = []
        #player.gold = 0

def heal(player, HP): # a heal function. HP should be an integer.
    player.health += HP
    if player.health > player.maxHp:
        player.health = player.maxHp
    baseM.showText(player, "you healed " + str(HP) + " health",screen)
    if player.alive == True:
        baseM.showText(player, "Current health: " + str(player.health),screen)

def damage(player, HP): # a damage function. HP should be an integer.
    player.health -= HP
    baseM.showText(player, "you took " + str(HP) + " damage",screen)
    checkDeath(player)
    if player.alive == True:
        baseM.showText(player, "Current health: " + str(player.health),screen)
    

def spendGold(player, cost): # A function for the player losing money. Returns False if the player doesn't have enough money to spend. ("cost" should be an integer.)
    if player.gold < cost:
        baseM.showText(player, "you don't have enough money",screen)
        return False
    else:
        player.gold -= cost
        baseM.showText(player, "you lose " + str(cost) + " gold",screen)
        baseM.showText(player, "Current gold: " + str(player.gold),screen)
        return True

def earnGold(player, gold): # A function for the player gaining money. ("gold" should be an integer.)
    player.gold += gold
    baseM.showText(player, "you gain " + str(gold) + " gold",screen)
    baseM.showText(player, "Current gold: " + str(player.gold),screen)


def addItem(player, item): #adds an item to the list of items
    player.items.append(item)
    baseM.showText(player, "the " + item.name + " was added to your inventory",screen)


def removeItem(player, item): #adds an item to the list of items. Returns False if the item doesn't exist in the inventory.
    if item in player.items:
        player.items.remove(item)
        baseM.showText(player, "you lost the " + item.name,screen)
        if item == "loincloth":
            baseM.showText(player, "you lost your loincloth! -1 to public decency!",screen)
        return True
    else:
        baseM.showText(player, "You don't have the " + item.name,screen)
        return False
        



#def update(player):  **OBSOLETE FUNCTION**
    #checkDeath(player)
    #checkDebt(player)

















