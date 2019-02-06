
class PChar(): #intializes the class. The Main handles this, so you don't need it in your room.
    def __init__(self):
        self.health = 100
        self.gold = 99
        self.items = ["loincloth"]
        self.alive = True

def checkDeath(Player): #checks if the player is dead. Handled automatically in the damage() function.
    if Player.health <= 0:
        death(Player)

def death(Player): # sets Player.alive to False. Handled automatically by the checkDeath() function.
#Note: your level should have a way to end if the player dies (if Player.alive == False) whenever the player takes damage.
    Player.alive = False

#def checkDebt(Player): **OBSOLETE FUNCTION**
 #   if Player.gold <= 0:
  #      
   #     print("You are in debt! The IRS has come to extort money out of you.") 
    #    print("you lose all your items and " + -Player.gold + " health.")
     #   if "loincloth" in Player.items:
      #      print("they even take your Loincloth! -1 to public decency") 
       # Player.health -= char.gold
        #Player.items = []
        #Player.gold = 0

def heal(Player, HP): # a heal function. HP should be an integer.
    Player.health += HP
    print("you healed " + str(HP) + " health")
    if Player.alive == True:
        print("Current health: " + str(Player.health))

def damage(Player, HP): # a damage function. HP should be an integer.
    Player.health -= HP
    print("you took " + str(HP) + " damage")
    checkDeath(Player)
    if Player.alive == True:
        print("Current health: " + str(Player.health))
    

def spendGold(Player, cost): # A function for the player losing money. Returns False if the player doesn't have enough money to spend. ("cost" should be an integer.)
    if Player.gold < cost:
        print("you don't have enough money")
        return False
    else:
        Player.gold -= cost
        print("you lose " + str(cost) + " gold")
        print("Current gold: " + str(Player.gold))
        return True

def earnGold(Player, gold): # A function for the player gaining money. ("gold" should be an integer.)
    Player.gold += gold
    print("you gain " + str(gold) + " gold")
    print("Current gold: " + str(Player.gold))


def addItem(Player, item): #adds an item to the list of items
    Player.items.append(item)
    print("the " + item + " was added to your inventory")


def removeItem(Player, item): #adds an item to the list of items. Returns False if the item doesn't exist in the inventory.
    if item in Player.items:
        Player.items.remove(item)
        print("you lost the " + item)
        if item == "loincloth":
            print("you lost your loincloth! -1 to public decency!")
        return True
    else:
        print("You don't have the " + item)
        return False
        



#def update(Player):  **OBSOLETE FUNCTION**
    #checkDeath(Player)
    #checkDebt(Player)
