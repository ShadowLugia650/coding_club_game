def playerhelp():
    print("game commands:")
    print("    \"help\"        opens the commands guide")
    print("    \"status\"      prints your health and gold")
    print("    \"inventory\"      prints your item list")

def status(Player):
    print("Health: " + str(Player.health))
    print("Gold: " + str(Player.gold))

def inventory(Player):
    for item in Player.items:
        print(item)

def testGold(Player):
    Player.gold += 1000

def testHP(Player):
    Player.health += 1000
    
def getInput(Player, outputs, prompt = ""): # a better Input function. Has built-in UI commands.
    output = False
    while output == False:
        console = input(prompt).lower()
        if console == "help":
            playerhelp()
        elif console == "status":
            status(Player)
        elif console == "inventory":
            inventory(Player)
        elif console == "testgold":
            testGold(Player)
        elif console == "testhp":
            testHP(Player)
        elif console in outputs:
            output = True
        else:
            print("not a valid input")
    return console


        
