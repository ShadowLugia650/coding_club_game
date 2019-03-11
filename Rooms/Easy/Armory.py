import sys
sys.path.insert(0, 'dependencies')
import baseM, itemStats
    
def pickWeapon(player):
    choice = input("[Glowing Sword, Glowing Shield, Glowing Orb]")
    if choice.title() in ["Glowing Sword", "Sword", "Attack", "Offense", "Damage"]:
        print("You pick up the glowing sword and leave the room.")
        
def bigManChoice2(player):
    choice = input("[Sword, Shield, Magic]")
    base = None
    spec = ""
    if choice.title() in ["Sword", "Attack", "Offense", "Damage"]:
        base = itemStats.basicSword
        spec = "self.name = 'Indestructible Sword'\nself.desc = 'A weapon created in the giant forge. It seems indestructible'\nself.damage = 15"
    elif choice.title() in ["Shield", "Defense", "Block", "Armor"]:
        base = itemStats.basicDefensiveItem
        spec = "self.name = 'Indestructible Shield'\nself.desc = 'A shield created in the giant forge. It seems indestructible'\nself.block = 15"
    elif choice.title() in ["Magic", "Abracadabra"]:
        base = itemStats.basicMagicItem
        spec = "self.name = 'Indestructible Staff'\nself.desc = 'A magical staff created in the giant forge. It seems indestructible'"
    else:
        baseM.checkCommands(choice, player)
        bigManChoice2(player)
    class customItem(base):
        def __init__(self):
            exec(spec)
            self.value = 177
    player.items.append(customItem())
        
def bigManChoice1(player):
    choice = input("[\"I'm just looking around.\", \"How do you deal with this temperature?\", \"I would like your assistance.\"]")
    if choice.title() in ["I'm Just Looking Around", "Im Just Looking Around", "Looking", "Around", "Just Looking Around", "Looking Around"]:
        print("\"LOOKING AROUND, HM? FEEL FREE TO TAKE ANYTHING YOU LIKE.\"")
        print("You walk around the hallway and notice a few glowing weapons resting against the wall.")
        pickWeapon(player)
    elif choice.title() in ["How Do You Deal With This Temperature", "Temp", "Temperature", "Heat", "Hot", "Warm"]:
        print("The voice laughs. \"TOO WARM FOR YOU? THE HEAT IS NECESSARY TO FORGE WEAPONRY WITH SUCH DURABILITY.\"")
        print("You look around and realize that many of the weapons on the walls have existed for centuries. Despite this, they all still seem sturdy and powerful.")
        print("")
    elif choice.title() in ["I Would Like Your Assistance", "Assistance", "Help"]:
        print("\"WHAT CAN I MAKE FOR YOU?\"")
        bigManChoice2(player)
    else:
        baseM.checkCommands(choice, player)
        bigManChoice1(player)
    
def run(player):
    print("You enter a large hallway with countless armaments of every kind covering the walls.")
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
        print("While many of the armaments stand over three times your height, a few smaller, glowing weapons catch your eye.")
        pickWeapon(player)
    elif choice.title() in ["Leave", "L"]:
        print("Afraid to continue into the heat, you hurry to the door and leave.")
    else:
        baseM.checkCommands(choice, player)
        run(player)
    return player
