import sys, random

sys.path.insert(0, 'dependencies')
import baseM, pScript, console
from itemStats import vorpalBlade

def run(player):
    response = ""
    cost = random.randint(8,15)
    print("Out from the darkness, a man in a hood approaches you.")
    while True:
        response = console.getInput(player, ["yes", "no"], "Pay " + str(cost) + " to listen to his story? ")
        if response.lower() == "yes":
            if pScript.spendGold(player, cost) == False:
                badEnd()
                return player
            if story(player, cost) == False:
                badEnd()
                return player
        if response.lower() == "no":
            badEnd()
            return player
        goodEnd(player)
        break

def goodEnd(player):
    print("Upon finishing his story, the mysterious traveller gives you a parting gift before disappearing back into the shadows.")
    pScript.addItem(player, vorpalBlade())

def badEnd():
    print("the man looks at you disappointedly, then retreats back to the shadows.")

def story(player, cost):
    text = ["I met a traveller from an antique land, \nWho said—“Two vast and trunkless legs of stone \nStand in the desert....",
        "Near them, on the sand, \nHalf sunk a shattered visage lies, whose frown, \nAnd wrinkled lip, and sneer of cold command....",
        "Tell that its sculptor well those passions read \nWhich yet survive, stamped on these lifeless things, \nThe hand that mocked them, and the heart that fed;",
        "And on the pedestal, these words appear:",
        "My name is Ozymandias, King of Kings; \nLook on my Works, ye Mighty, and despair!",
        "Nothing beside remains. Round the decay \n Of that colossal Wreck, boundless and bare \nThe lone and level sands stretch far....",
        "away." ]
    for item in text:
        if item != text[0]:
            cost = round(cost * (random.random()+ 1))
            text = "Pay " + str(cost) + " to continue? "
            response = console.getInput(player, ["yes", "no"], text)
            if response == "no":
                return False
            if pScript.spendGold(player, cost) == False:
                return False
            print("\nThe hooded man continues his story:")
        else:
            print("\nThe hooded man begins:")
        print(item)
    return True

        


