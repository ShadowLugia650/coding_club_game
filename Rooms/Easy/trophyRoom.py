import itemStats
import baseM
def run(player):
    commonItems = [itemStats.shovel(), itemStats.healthPotion(), itemStats.brokenSword(), itemStats.dullKnife(), itemStats.rustyPitchfork(), itemStats.baseballBat(), itemStats.cardboardShield(), itemStats.tinyShield()]
    rareItems = [itemStats.staffOfGold(), itemStats.sword(), itemStats.shield(), itemStats.abandonedAxe(), itemStats.warhammer(), itemStats.diamondSword(), itemStats.glowingOrb()]
    legendaryItems = [itemStats.epiTome()]
    print("The passageway opens up into a small, cramped, room lined with rusty weapons and tools.")
    choice=input("Do you want to look around for something useful?")
    while True:
        if choice in ["yes", "y", "si", "of course"]:
            while True:
                print("Grab many random items, or search carefully for specific useful items?")
                choice = input("[Grab random, search for useful]")
                
