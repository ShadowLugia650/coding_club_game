import sys, random, discord
from discord.ext import commands
from discord.ext.commands import Bot

sys.path.insert(0, 'dependencies')
import console, pScript, baseM, itemStats

sys.path.insert(0, 'Rooms/Easy')
import shopM, battleZombomanM, bestRoomRC
easy= [shopM, battleZombomanM, bestRoomRC]
sys.path.insert(0, 'Rooms/Medium')
import strangerJGv1, battleGhoulM, mirrorsM, lavaroomRCv1, skeletonCalvin
med = [strangerJGv1, battleGhoulM, mirrorsM, lavaroomRCv1, skeletonCalvin]
sys.path.insert(0, 'Rooms/Hard')
import owM, Collector, demonicWarrior
hard= [owM, Collector, demonicWarrior]
sys.path.insert(0, 'Rooms/Impossible')
impossible = []

Client = discord.Client()
client = commands.Bot(command_prefix=commands.when_mentioned_or('>'))
Player = pScript.PChar()
levels = easy
consol = ""
rounds = 0

@client.command(pass_context=True)
async def cont(ctx):
    """Continue the story"""
    
@client.command(pass_context=True)
async def view(ctx, *, item):
    """View an item and its description"""
    itm = eval(baseM.strToClsNm(item))()
    if itm is not None:
        await client.say("Description:\n{}".format(itm.desc))
        #await client.send_file(ctx.message.channel, "resources/{}.png".format(itm.name)) #sends picture

baseM.initIntro(Player)
while Player.alive:
    room = levels[random.randint(0, (len(levels)-1))]
    consol = console.getInput(Player, ["yes", "no"], "next room? ")
    if consol.lower() in ["yes", "y", "ok", "sure", "yeah", "yay"]:
        room.run(Player)
        rounds += 1
        for i in Player.items:
            try:
                if issubclass(i, itemStats.basicItem()):
                    i.onFloorClimb(Player)
            except TypeError:
                pass
    else:
        break
    if Player.alive == False:
        print("You have died.")
    if rounds == 3:
        levels += med
    elif rounds == 20:
        levels += hard
print("Game over.")
print("rooms cleared:  " + str(rounds))
print("Ending gold:    " + str(Player.gold))
print("Ending items:")
for i in Player.items:
    print("- {}".format(i))
input()



