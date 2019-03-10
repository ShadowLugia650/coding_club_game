def run(player):
    input("You see a large grey structure looming in the distance.. [Approach]") #This is the intro.. Needs work...
    input("As you approach, a giant stone door slowly rises, revealing a dark room, faintly lit by the setting Sun outside... [Continue]")
    input("You see a note laying atop a pile of frayed cloth armor and a rusty sword.. [Read note]")
    input("The door slams shut behind you! Deep in the dungeon you see a dim light... [Approach]")
    choice = input("You take the torch, wondering what lies within the dungeon... [Return to Note, Continue into Dungeon]")
    while True:
        if choice.title() in ["Return", "R", "Return To Note", "Note"]:
            input("You walk back to the note, taking it along with the armor and the sword.. [Continue]")
            player.items.append(letterFromTheDeceased())
            print("Letter From the Deceased was added to your inventory! Use [Inventory] to read it")
            player.items.append(rustySword())
            print("Rusty Sword was added to your inventory! You're going to need it...")
            player.items.append(frayedClothArmor())
            print("Frayed Cloth was added to your inventory!")
            break
        elif choice.title() in ["Continue", "C", "Continue Into Dungeon", "Dungeon"]:
            input("You continue walking into the dungeon and begin to feel very cold...[Continue]")
            player.health -= 3
            print("You regret not taking the cloth and sword.")
            break
        checkCommands(choice, player)
        choice = input("Continue into the dungeon or return to read the note?")
    return player
