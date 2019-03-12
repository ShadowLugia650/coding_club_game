import itemStats
import baseM
def run(player):
    commonItems = [itemStats.shovel(), itemStats.healthPotion(), itemStats.brokenSword(), itemStats.dullKnife(), itemStats.rustyPitchfork(), itemStats.baseballBat(), itemStats.cardboardShield(), itemStats.tinyShield()]
    rareItems = [itemStats.staffOfGold(), itemStats.sword(), itemStats.shield(), itemStats.abandonedAxe(), itemStats.warhammer(), itemStats.diamondSword(), itemStats.glowingOrb()]
    legendaryItems = [itemStats.epiTome()]
    trueItems = []
    while True:
        print("The passageway opens up into a small, cramped, room lined with rusty weapons and tools.")
        choice=input("Do you want to look around for something useful?")
        if choice in ["yes", "y", "si", "of course"]:
            while True:
                print("Grab many random items, or search carefully for specific useful items?")
                choice = input("[Grab random, search for useful]")
                if choice.lower() in ["grab random", "grab", "random"]:
                    for i in range(4):
                        trueItems+=commonItems
                    trueItems+=rareItems
                    for i in range(4):
                        addedItem = random.choice(trueItems)
                        print(addedItem.name+" was added to your inventory! /n")
                        player.items.append(addedItem)
                    return player
                elif choice.lower() in ["search for useful","search", "useful"]:
                    for i in range(3):
                        trueItems+=rareItems
                    trueItems+=legendaryItems
                    addedItem = random.choice(trueItems)
                    print(addedItem.name+" was added to your inventory! /n")
                    player.items.append(addedItem)
                    return player
                else:
                    print("Sorry! That is not one of your choices")
        elif choice in ["no", "n","never"]:
            print("You exit the room.")
            return player
        else:
            print("Sorry! That is not one of your choices")
