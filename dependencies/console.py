import baseM
def playerhelp():
    print("game commands:")
    print("    \"help\"        opens the commands guide")
    print("    \"status\"      prints your health and gold")
    print("    \"inventory\"   prints your item list")
    print("    \"options\"     prints the listed inputs you can make")
    print("    \"testgold\"    lets you input a new gold amount. Big errors if you don't enter an int")
    print("    \"testhp\"      lets you input a new health amount. Big errors if you don't enter an int")

def status(Player):
    print("Health: " + str(Player.health))
    print("Gold: " + str(Player.gold))

def inventory(Player):
    for item in Player.items:
        print(item)

def testGold(Player, x):
    Player.gold = int(x)

def testHP(Player, y):
    Player.health = int(y)
    
def getInput(Player, outputs, prompt = ""): # a better Input function. Has built-in UI commands.
    output = False
    while output == False:
        console = input(prompt)
        if console.lower() in ["help", "?"]:
            playerhelp()
        elif console.lower() in ["status", "stat", "me", "stats"]:
            status(Player)
        elif console.lower() in ["inventory", "inv", "items", "bag"]:
            inventory(Player)
        elif console.lower() in ["options", "opt", "options?", "opt?"]:
            print(outputs)
        elif console.lower() in outputs:
            output = True
        else:
            baseM.checkCommands(console, Player)
    return console.lower()

def delayPrint(Player, text = ""):
    print(text)
    input()
