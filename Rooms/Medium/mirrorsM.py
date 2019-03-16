import sys, random

sys.path.insert(0, 'dependencies')
import baseM, itemStats
from pScript import PChar

def initPlayers():
    players = []
    t = []
    for i in range(5):
        players.append(PChar())
        t.append('')
    #First Player: The Ironclad
    players[0].health = 120
    players[0].maxHp = 120
    players[0].items = [itemStats.heavySword(), itemStats.basicDefensiveItem(), itemStats.steelPlateArmor()]
    t[0] = "heavy, yet strong"
    #Second Player: The Silent
    players[1].health = 90
    players[1].maxHp = 90
    players[1].items = [itemStats.shiv(), itemStats.shiv(), itemStats.cloak()]
    t[1] = "agile and deadly"
    #Third Player: The Defect?
    players[2].items = [itemStats.orbOfThunder(), itemStats.orbOfVampirism()]
    t[2] = "robotic, but magical"
    #Fourth Player: The lost traveler
    players[3].health = 40
    players[3].gold = 12
    players[3].items = [itemStats.wornJournal(), itemStats.loincloth(), itemStats.rustySword()]
    t[3] = "lost and afraid"
    #Fifth Player: The merchant
    players[4].gold = 700
    players[4].items = []
    t[4] = "wealthy"
    #Sixth Player: and more..
    players2 = baseM.readStoredPlayers("data/mirrorsM.txt")
    for i in players2:
        t.append("different, but familiar..")
    players += players2
    return players, t

def run(player, screen):
    baseM.showText("You enter a room full of mirrors. Everywhere you look you see yourself, yet they all seem.. distorted...",screen)
    baseM.showText("You walk up to a mirror and place your hand on it. You feel your hand start to phase through...",screen)
    choice = baseM.showText("What do you do? [Continue, Leave]\n",screen)
    if choice.title() in ["Continue", "C"]:
        baseM.showText("You continue, pushing through the mirror and reach the other side.",screen)
        ps, texts = initPlayers()
        baseM.writePlayer(player, "data/mirrorsM.txt")
        p = random.choice(ps)
        txt = texts[ps.index(p)]
        baseM.showText("You look back at the mirror from which you came and see yourself there.",screen)
        baseM.showText("As you leave the room, you feel... {}..[Continue]".format(txt,screen),screen),screen)
        player.gold = p.gold
        for i in range(3):
            player.items.remove(random.choice(player.items))
        player.items += p.items
        player.health = p.health
        return player
    elif choice.title() in ["Leave", "L"]:
        baseM.showText("You jump back, startled, feeling a sharp pain in your hand.",screen)
        player.health -= 12
        baseM.checkPlayer(player, screen)
        if player.alive:
            baseM.showText("You leave the room as if nothing has happened..[Continue]",screen)
        else:
            return player
    else:
        baseM.checkCommands(choice, player)
        run(player, screen)
    return player





