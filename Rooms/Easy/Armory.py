import sys
sys.path.insert(0, 'dependencies')
import baseM, itemStats

class customItem(itemStats.basicSword):
    def __init__(self):
        self.name = ""
        self.desc = "A weapon created in the giant forge.. It seems indestructible."
        self.damage = 0
        self.value = 177

def bigManChoice1(player):
    choice = input("[\"I'm just looking around.\", \"How do you deal with this temperature?\", \"I would like your assistance.\"]")
    
def pickWeapon(player):
    choice = input("[]")
    
def run(player):
    print("You enter a large hallway with countless weapons of every kind covering the walls.")
    print("Near the center of the hall you notice an enormous anvil with an equally enormous hammer resting on it.")
    print("As you approach the anvil, the air around you seems to grow warmer and warmer. The blistering heat seems to lightly singe your skin..")
    choice = input("[Continue to Anvil, Inspect Walls, Leave]")
    if choice.title() in ["Continue To Anvil", "Continue", "Anvil", "Hammer", "C"]:
        print("You continue walking toward the anvil and begin to wonder how any creature could survive in these feverish temperatures.")
        print("At last! You reach the anvil! As you gaze in wonder at the sheer magnitude of the anvil and its hammer, a loud, booming voice distracts you from your thoughts.")
        print("\"WELCOME MORTAL! WHAT BRINGS YOU HERE TODAY?\"")
        print("While loud, the voice sounds relatively harmless and inviting.")
        bigManChoice1(player)
    elif choice.title() in ["Inspect Walls", "Inspect", "Walls", "I"]:
        print("Moving away from the scorching heat of the anvil, you admire the masterful craftmanship of the weapons on the walls.")
        print("While many of the weapons stand over three times your height, a few smaller, glowing weapons catch your eye.")
        pickWeapon(player)
    elif choice.title() in ["Leave", "L"]:
        print("Afraid to continue into the heat, you hurry to the door and leave.")
    else:
        baseM.checkCommands(choice, player)
        run(player)
    return player
