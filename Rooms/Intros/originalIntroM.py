import sys
sys.path.insert(0, 'dependencies')
import itemStats, baseM
def run(player, screen):
    baseM.showText(player, "You see a large grey structure looming in the distance.. [Approach]",screen) #This is the intro.. Needs work...
    baseM.showText(player, "As you approach, a giant stone door slowly rises, revealing a dark room, faintly lit by the setting Sun outside... [Continue]",screen)
    baseM.showText(player, "You see a note laying atop a pile of frayed cloth armor and a rusty sword.. [Read note]",screen)
    baseM.showText(player, "The door slams shut behind you! Deep in the dungeon you see a dim light... [Approach]",screen)
    choice = baseM.showText(player, "You take the torch, wondering what lies within the dungeon... [Return to Note, Continue into Dungeon]",screen)
    player.items.append(itemStats.torch())
    while True:
        if choice.title() in ["Return", "R", "Return To Note", "Note"]:
            baseM.showText(player, "You walk back to the note, taking it along with the armor and the sword.. [Continue]",screen)
            player.items.append(itemStats.letterFromTheDeceased())
            baseM.showText(player, "Letter From the Deceased was added to your inventory! Use [Inventory] to read it",screen)
            player.items.append(itemStats.rustySword())
            baseM.showText(player, "Rusty Sword was added to your inventory! You're going to need it...",screen)
            player.items.append(itemStats.frayedClothArmor())
            baseM.showText(player, "Frayed Cloth was added to your inventory!",screen)
            break
        elif choice.title() in ["Continue", "C", "Continue Into Dungeon", "Dungeon"]:
            baseM.showText(player, "You continue walking into the dungeon and begin to feel very cold...[Continue]",screen)
            player.health -= 3
            baseM.showText(player, "You regret not taking the cloth and sword.",screen)
            break
        baseM.checkCommands(choice, player,screen)
        choice = baseM.showText(player, "return to read the note or continue into the dungeon? [Return to Note, Continue into Dungeon]",screen)
    return player















