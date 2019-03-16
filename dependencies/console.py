import baseM
def playerhelp(screen):
    baseM.showText("""game commands:
    "help"        opens the commands guide
    "status"      prints your health and gold
    "inventory"   prints your item list
    "inspect"     view the description of an item
    "drink"       drink a potion""",screen) # fix for pygame mode
#    baseM.showText("    \"testgold\"    lets you input a new gold amount. Big errors if you don't enter an int",screen)
#    baseM.showText("    \"testhp\"      lets you input a new health amount. Big errors if you don't enter an int",screen)
#    baseM.showText("    \"options\"     prints the listed inputs you can make",screen)

def status(Player,screen):
    baseM.showText("Health: " + str(Player.health),screen)
    baseM.showText("Gold: " + str(Player.gold),screen)

def inventory(Player,screen):
    for item in Player.items:
        baseM.showText(item,screen)
def curses(Player,screen):
    for curse in Player.curses:
        baseM.showText(curse,screen)
        
def testGold(Player, x):
    Player.gold = int(x)

def testHP(Player, y):
    Player.health = int(y)
    
def getInput(Player, outputs, prompt = "", screen = None): # a better Input function. Has built-in UI commands.
    output = False
    while output == False:
        console = baseM.showText(prompt,screen)
        if console.lower() in ["help", "?"]:
            playerhelp()
        elif console.lower() in ["status", "stat", "me", "stats"]:
            status(Player)
        elif console.lower() in ["inventory", "inv", "items", "bag"]:
            inventory(Player)
        elif console.lower() in ["curses", "curse", "crs"]:
            curses(Player)
        elif console.lower() in ["options", "opt", "options?", "opt?"]:
            baseM.showText(outputs,screen)
        elif console.lower() in outputs:
            output = True
        else:
            baseM.checkCommands(console, Player,screen)
    return console.lower()

def delayPrint(Player, text = "", screen = None):
    baseM.showText(text,screen)
    baseM.showText()







