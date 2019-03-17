import itemStats
import baseM
import random
def run(player, screen):
    commonItems = [itemStats.shovel(), itemStats.healthPotion(), itemStats.brokenSword(), itemStats.dullKnife(), itemStats.rustyPitchfork(), itemStats.baseballBat(), itemStats.cardboardShield(), itemStats.tinyShield()]
    rareItems = [itemStats.staffOfGold(), itemStats.sword(), itemStats.shield(), itemStats.abandonedAxe(), itemStats.warhammer(), itemStats.diamondSword(), itemStats.glowingOrb()]
    legendaryItems = [itemStats.epiTome()]
    trueItems = []
    while True:
        baseM.showText(player, "The passageway opens up into a small, cramped, room lined with rusty weapons and tools.",screen)
        choice=baseM.showText(player, "Do you want to look around for something useful?",screen)
        if choice in ["yes", "y", "si", "of course"]:
            while True:
                baseM.showText(player, "Grab many random items, or search carefully for specific useful items?",screen)
                choice = baseM.showText(player, "[Grab random, search for useful]",screen)
                if choice.lower() in ["grab random", "grab", "random"]:
                    for i in range(4):
                        trueItems+=commonItems
                    trueItems+=rareItems
                    for i in range(4):
                        addedItem = random.choice(trueItems)
                        baseM.showText(player, addedItem.name+" was added to your inventory! /n",screen)
                        player.items.append(addedItem)
                    return player
                elif choice.lower() in ["search for useful","search", "useful"]:
                    for i in range(3):
                        trueItems+=rareItems
                    trueItems+=legendaryItems
                    addedItem = random.choice(trueItems)
                    baseM.showText(player, addedItem.name+" was added to your inventory! /n",screen)
                    player.items.append(addedItem)
                    return player
                else:
                    baseM.showText(player, "Sorry! That is not one of your choices",screen)
        elif choice in ["no", "n","never"]:
            baseM.showText(player, "You exit the room.",screen)
            return player
        else:
            baseM.showText(player, "Sorry! That is not one of your choices",screen)















