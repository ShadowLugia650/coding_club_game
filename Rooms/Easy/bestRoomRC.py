import itemStats
import baseM
#Needs to be updated to have a loop in the first prompt for user input
def run(player, screen):
    baseM.showText(player, """The hallway opens up into a fork.
Down one path you see a fountain bubbling with clear, pure, water, and down
the other you see a golden door.""", screen)
    while True:
        choice = baseM.showText(player, "Choose your path [Fountain, Gold]",screen).title()
        if choice in ["Fountain","F"]:
            while True:
                choice = baseM.showText(player, "Do you wish to drink from the fountain? [yes, no]",screen)
                if choice in ["yes", "y","okay","ok"]:
                    baseM.showText(player, "You feel the water purify and heal your body",screen)
                    baseM.showText(player, "You were healed to full health!",screen)
                    player.health = player.maxHp
                    return player
                elif choice in ["no", "n"]:
                    baseM.showText(player, "You continue on your way, wondering what could have been",screen)
                    return player
                else:
                    baseM.showText(player, "Sorry, that is not one of your choices",screen)
            break
        elif choice in ["Gold", "G"]:
            baseM.showText(player, """You reach the golden door. What would you like to do?
Press 1 to knock on the door
Press 2 to try to break open the door
Press 3 to cut off pieces of gold and steal them
Press 4 to search the room for a key
Press 5 to leave""", screen)
            while True:
                choice=baseM.showText(player, "[Knock on the door, Break open the door, Cut off pieces, Search for a key, Leave]",screen).lower()
                if choice in ["1", "one", "knock"]:
                    baseM.showText(player, """The door opens into a room full of treasure. Gold coins are scattered throughout the chamber, but two incongruencies catch your eye.
A pair of large dice lie near the right wall of the room, while a staff made of pure gold leans against the left wall.
What would you like to do?
Press 1 to gather gold coins, then leave
Press 2 to investigate the dice
Press 3 to take the staff""", screen)
                    while True:
                        choice=baseM.showText(player, "[Gather coins, Investigate dice, Take staff]",screen).lower()
                        if choice in ["1", "one", "gather"]:
                            baseM.showText(player, "Good thing you didn't try to desecrate the door. Cheaters never prosper",screen)
                            baseM.showText(player, "You gained 150 gold!",screen)
                            player.gold+=150
                            return player
                        elif choice in ["2", "two", "investigate"]:
                            baseM.showText(player, "You roll the dice and get a 6!",screen)
                            baseM.showText(player, "Staff of Luck was added to your inventory",screen)
                            player.items.append(itemStats.staffOfLuck())
                            return player
                        elif choice in ["3", "three", "take"]:
                            baseM.showText(player, "You pick up the staff",screen)
                            baseM.showText(player, "Staff of Gold was added to your inventory!",screen)
                            player.items.append(itemStats.staffOfGold())
                            return player
                        else:
                            baseM.showText(player, "Sorry, That is not one of your choices",screen)
                    break
                elif choice in ["2", "two", "break"]:
                    baseM.showText(player, "You chip off some gold but ultimately accomplish nothing. You leave, disappointed.",screen)
                    player.gold+=15
                    return player
                elif choice in ["3", "three", "steal"]:
                    baseM.showText(player, "You gain 50 gold but ruin the door in the process",screen)
                    player.gold+=50
                    return player
                elif choice in ["4", "four", "search"]:
                    baseM.showText(player, "Though you don't find a key, you do find a dusty magic wand leaning in the corner.",screen)
                    baseM.showText(player, "Wand of Confusion was added to your inventory!",screen)
                    player.items.append(itemStats.wandOfConfusion())
                    return player
                elif choice in ["5", "five", "leave"]:
                    baseM.showText(player, "You leave the room.",screen)
                    return player
                else:
                    baseM.showText(player, "Sorry, that is not one of your choices",screen)
        else:
            baseM.showText(player, "Sorry, that is not one of your choices",screen)
        


















