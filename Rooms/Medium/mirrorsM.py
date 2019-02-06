import sys, random

sys.path.insert(0, 'dependencies')
import baseM
from pScript import PChar

def initPlayers():
    players = []
    t = []
    for i in range(5):
        players.append(PChar())
        t.append('')
    #First Player: The Ironclad
    players[0].health = 120
    players[0].items = ["Heavy Sword", "Shield", "Steel-Plate Armor"]
    t[0] = "heavy, yet strong"
    #Second Player: The Silent
    players[1].health = 90
    players[1].items = ["Shiv", "Cloak"]
    t[1] = "agile and deadly"
    #Third Player: The Defect?
    players[2].health = 100
    players[2].items = [""]
    t[2] = "robotic"
    #Fourth Player: The lost traveler
    players[3].health = 40
    players[3].gold = 12
    players[3].items = ["Worn Journal", "Loincloth", "Rusty Knife"]
    t[3] = "lost and afraid"
    #Fifth Player: The merchant
    players[4].gold = 700
    players[4].items = [""]
    t[4] = "wealthy"
    #Sixth Player: and more..
    players2 = baseM.readStoredPlayers("data/mirrorsM.txt")
    for i in players2:
        t.append("different, but familiar..")
    players += players2
    return players, t

def run(player):
    print("You enter a room full of mirrors. Everywhere you look you see yourself, yet they all seem.. distorted...")
    print("You walk up to a mirror and place your hand on it. You feel your hand start to phase through...")
    choice = input("What do you do? [Continue, Leave]\n")
    if choice.title() in ["Continue", "C"]:
        print("You continue, pushing through the mirror and reach the other side.")
        ps, texts = initPlayers()
        baseM.writePlayer(player, "data/mirrorsM.txt")
        p = random.choice(ps)
        txt = texts[ps.index(p)]
        print("You look back at the mirror from which you came and see yourself there.")
        input("As you leave the room, you feel... {}..[Continue]".format(txt))
        player.gold = p.gold
        player.items = p.items
        player.health = p.health
        return player
    elif choice.title() in ["Leave", "L"]:
        print("You jump back, startled, feeling a sharp pain in your hand.")
        player.health -= 12
        baseM.checkPlayer(player)
        if player.alive:
            input("You leave the room as if nothing has happened..[Continue]")
        else:
            return player
    else:
        baseM.checkCommands(choice, player)
        run(player)
    return player
