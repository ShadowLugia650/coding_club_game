import itemStats
import baseM
#Needs to be updated to have a loop in the first prompt for user input
def run(player, screen):
    baseM.showText("""The hallway opens up into a fork.
Down one path you see a fountain bubbling with clear, pure, water, and down
the other you see a golden door.""")
    while True:
        choice = baseM.showText("Choose your path [Fountain, Gold]").title()
        if choice in ["Fountain","F"]:
            while True:
                baseM.showText("Do you wish to drink from the fountain? [yes, no]")
                choice=baseM.showText()
                if choice in ["yes", "y","okay","ok"]:
                    baseM.showText("You feel the water purify and heal your body")
                    baseM.showText("You were healed to full health!")
                    player.health = player.maxHp
                    return player
                elif choice in ["no", "n"]:
                    baseM.showText("You continue on your way, wondering what could have been")
                    return player
                else:
                    baseM.showText("Sorry, that is not one of your choices")
            break
        elif choice in ["Gold", "G"]:
            baseM.showText("""You reach the golden door. What would you like to do?
Press 1 to knock on the door
Press 2 to try to break open the door
Press 3 to cut off pieces of gold and steal them
Press 4 to search the room for a key
Press 5 to leave""")
            while True:
                choice=baseM.showText("[Knock on the door, Break open the door, Cut off pieces, Search for a key, Leave]").lower()
                if choice in ["1", "one", "knock"]:
                    baseM.showText("""The door opens into a room full of treasure. Gold coins are scattered throughout the chamber, but two incongruencies catch your eye.
A pair of large dice lie near the right wall of the room, while a staff made of pure gold leans against the left wall.
What would you like to do?
Press 1 to gather gold coins, then leave
Press 2 to investigate the dice
Press 3 to take the staff""")
                    while True:
                        choice=baseM.showText("[Gather coins, Investigate dice, Take staff]").lower()
                        if choice in ["1", "one", "gather"]:
                            baseM.showText("Good thing you didn't try to desecrate the door. Cheaters never prosper")
                            baseM.showText("You gained 150 gold!")
                            player.gold+=150
                            return player
                        elif choice in ["2", "two", "investigate"]:
                            baseM.showText("You roll the dice and get a 6!")
                            baseM.showText("Staff of Luck was added to your inventory")
                            player.items.append(itemStats.staffOfLuck())
                            return player
                        elif choice in ["3", "three", "take"]:
                            baseM.showText("You pick up the staff")
                            baseM.showText("Staff of Gold was added to your inventory!")
                            player.items.append(itemStats.staffOfGold())
                            return player
                        else:
                            baseM.showText("Sorry, That is not one of your choices")
                    break
                elif choice in ["2", "two", "break"]:
                    baseM.showText("You chip off some gold but ultimately accomplish nothing. You leave, disappointed.")
                    player.gold+=15
                    return player
                elif choice in ["3", "three", "steal"]:
                    baseM.showText("You gain 50 gold but ruin the door in the process")
                    player.gold+=50
                    return player
                elif choice in ["4", "four", "search"]:
                    baseM.showText("Though you don't find a key, you do find a dusty magic wand leaning in the corner.")
                    baseM.showText("Wand of Confusion was added to your inventory!")
                    player.items.append(itemStats.wandOfConfusion())
                    return player
                elif choice in ["5", "five", "leave"]:
                    baseM.showText("You leave the room.")
                    return player
                else:
                    baseM.showText("Sorry, that is not one of your choices")
        else:
            baseM.showText("Sorry, that is not one of your choices")
        




