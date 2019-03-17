import baseM
def playerhelp(screen):
    baseM.showText(None, """game commands:
    "help"        opens the commands guide
    "status"      prints your health and gold
    "inventory"   prints your item list
    "inspect"     view the description of an item
    "drink"       drink a potion""",screen) # fix for pygame mode
#    baseM.showText(player, "    \"testgold\"    lets you input a new gold amount. Big errors if you don't enter an int",screen)
#    baseM.showText(player, "    \"testhp\"      lets you input a new health amount. Big errors if you don't enter an int",screen)
#    baseM.showText(player, "    \"options\"     prints the listed inputs you can make",screen)

def status(player,screen):
    baseM.showText(player, "Health: " + str(player.health),screen)
    baseM.showText(player, "Gold: " + str(player.gold),screen)

def inventory(player,screen):
    for item in player.items:
        baseM.showText(player, item.__str__(),screen)
def curses(player,screen):
    for curse in player.curses:
        baseM.showText(player, curse.__str__(),screen)
        
def testGold(player, x):
    player.gold = int(x)

def testHP(player, y):
    player.health = int(y)
    
def getInput(player, outputs, prompt = "", screen = None): # a better Input function. Has built-in UI commands.
    output = False
    while output == False:
        console = baseM.showText(player, prompt,screen)
        if console.lower() in ["help", "?"]:
            playerhelp()
        elif console.lower() in ["status", "stat", "me", "stats"]:
            status(player, screen)
        elif console.lower() in ["inventory", "inv", "items", "bag"]:
            inventory(player, screen)
        elif console.lower() in ["curses", "curse", "crs"]:
            curses(player, screen)
        elif console.lower() in ["options", "opt", "options?", "opt?"]:
            baseM.showText(player, outputs,screen)
        elif console.lower() in outputs:
            output = True
        else:
            baseM.checkCommands(console, player,screen)
    return console.lower()

def delayPrint(player, text = "", screen = None):
    baseM.showText(player, text,screen)
    baseM.showText()

























