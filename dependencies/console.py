import baseM
def playerhelp():
    baseM.showText("game commands:")
    baseM.showText("    \"help\"        opens the commands guide")
    baseM.showText("    \"status\"      prints your health and gold")
    baseM.showText("    \"inventory\"   prints your item list")
#    baseM.showText("    \"options\"     prints the listed inputs you can make")
    baseM.showText("    \"inspect\"     view the description of an item")
    baseM.showText("    \"drink\"       drink a potion")
#    baseM.showText("    \"testgold\"    lets you input a new gold amount. Big errors if you don't enter an int")
#    baseM.showText("    \"testhp\"      lets you input a new health amount. Big errors if you don't enter an int")

def status(Player):
    baseM.showText("Health: " + str(Player.health))
    baseM.showText("Gold: " + str(Player.gold))

def inventory(Player):
    for item in Player.items:
        baseM.showText(item)
def curses(Player):
    for curse in Player.curses:
        baseM.showText(curse)
        
def testGold(Player, x):
    Player.gold = int(x)

def testHP(Player, y):
    Player.health = int(y)
    
def getInput(Player, outputs, prompt = ""): # a better Input function. Has built-in UI commands.
    output = False
    while output == False:
        console = baseM.showText(prompt)
        if console.lower() in ["help", "?"]:
            playerhelp()
        elif console.lower() in ["status", "stat", "me", "stats"]:
            status(Player)
        elif console.lower() in ["inventory", "inv", "items", "bag"]:
            inventory(Player)
        elif console.lower() in ["curses", "curse", "crs"]:
            curses(Player)
        elif console.lower() in ["options", "opt", "options?", "opt?"]:
            baseM.showText(outputs)
        elif console.lower() in outputs:
            output = True
        else:
            baseM.checkCommands(console, Player)
    return console.lower()

def delayPrint(Player, text = ""):
    baseM.showText(text)
    baseM.showText()



