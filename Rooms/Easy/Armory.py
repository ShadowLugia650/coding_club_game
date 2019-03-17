import sys
sys.path.insert(0, 'dependencies')
import baseM, itemStats
    
def pickWeapon(player, screen):
    choice = baseM.showText(player, "[Glowing Sword, Glowing Shield, Glowing Orb]",screen)
    if choice.title() in ["Glowing Sword", "Sword", "Attack", "Offense", "Damage"]:
        baseM.showText(player, "You pick up the glowing sword and leave the room.",screen)
        player.items.append(itemStats.glowingSword())
    elif choice.title() in ["Glowing Shield", "Shield", "Defense", "Block", "Armor"]:
        baseM.showText(player, "You pick up the glowing shield and leave the room.",screen)
        player.items.append(itemStats.glowingShield())
    elif choice.title() in ["Glowing Orb", "Orb", "Abracadabra", "Magic"]:
        baseM.showText(player, "You pick up the glowing orb and leave the room.",screen)
        player.items.append(itemStats.glowingOrb())
    else:
        baseM.checkCommands(choice, player,screen)
        pickWeapon(player, screen)
        
def bigManChoice2(player, screen):
    choice = baseM.showText(player, "[Sword, Shield, Magic]",screen)
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
        baseM.checkCommands(choice, player,screen)
        bigManChoice2(player, screen)
    class customItem(base):
        def __init__(self):
            exec(spec)
            self.value = 177
    player.items.append(customItem())
    baseM.showText(player, "You obtained the {}!".format(customItem().name),screen)
        
def bigManChoice1(player, screen):
    choice = baseM.showText(player, "[\"I'm just looking around.\", \"How do you deal with this temperature?\", \"I would like your assistance.\"]",screen)
    if choice.title() in ["I'm Just Looking Around", "Im Just Looking Around", "Looking", "Around", "Just Looking Around", "Looking Around"]:
        baseM.showText(player, "\"LOOKING AROUND, HM? FEEL FREE TO TAKE ANYTHING YOU LIKE.\"",screen)
        baseM.showText(player, "You walk around the hallway and notice a few glowing weapons resting against the wall.",screen)
        pickWeapon(player, screen)
    elif choice.title() in ["How Do You Deal With This Temperature", "Temp", "Temperature", "Heat", "Hot", "Warm"]:
        baseM.showText(player, "The voice laughs. \"TOO WARM FOR YOU? THE HEAT IS NECESSARY TO FORGE WEAPONRY WITH SUCH DURABILITY.\"",screen)
        baseM.showText(player, "You look around and realize that many of the weapons on the walls have existed for centuries. Despite this, they all still seem sturdy and powerful.",screen)
        baseM.showText(player, "Suddenly, ",screen)
    elif choice.title() in ["I Would Like Your Assistance", "Assistance", "Help"]:
        baseM.showText(player, "\"WHAT CAN I MAKE FOR YOU?\"",screen)
        bigManChoice2(player, screen)
    else:
        baseM.checkCommands(choice, player,screen)
        bigManChoice1(player, screen)
    
def run(player, screen):
    baseM.showText(player, "You enter a large hallway with countless armaments of every kind covering the walls.",screen)
    baseM.showText(player, "Near the center of the hall you notice an enormous anvil with an equally enormous hammer resting on it.",screen)
    baseM.showText(player, "As you approach the anvil, the air around you seems to grow warmer and warmer. The blistering heat seems to lightly singe your skin..",screen)
    choice = baseM.showText(player, "[Continue to Anvil, Inspect Walls, Leave]",screen)
    if choice.title() in ["Continue To Anvil", "Continue", "Anvil", "Hammer", "C"]:
        baseM.showText(player, "You continue walking toward the anvil and begin to wonder how any creature could survive in these feverish temperatures.",screen)
        baseM.showText(player, "At last! You reach the anvil! As you gaze in wonder at the sheer magnitude of the anvil and its hammer, a loud, booming voice distracts you from your thoughts.",screen)
        baseM.showText(player, "\"WELCOME MORTAL! WHAT BRINGS YOU HERE TODAY?\"",screen)
        baseM.showText(player, "While loud, the voice sounds relatively harmless and inviting.",screen)
        bigManChoice1(player, screen)
    elif choice.title() in ["Inspect Walls", "Inspect", "Walls", "I"]:
        baseM.showText(player, "Moving away from the scorching heat of the anvil, you admire the masterful craftmanship of the weapons on the walls.",screen)
        baseM.showText(player, "While many of the armaments stand over three times your height, a few smaller, glowing weapons catch your eye.",screen)
        pickWeapon(player, screen)
    elif choice.title() in ["Leave", "L"]:
        baseM.showText(player, "Afraid to continue into the heat, you hurry to the door and leave.",screen)
    else:
        baseM.checkCommands(choice, player,screen)
        run(player, screen)
    return player




























