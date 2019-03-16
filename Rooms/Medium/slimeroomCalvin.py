import random, sys
sys.path.insert(0, 'dependencies')
import baseM, itemStats

#class player:
 # def __init__(self):
  #  self.health = 10
   # self.gold = 0
    #self.items = ["axe", "loincloth", "torch", "shield"]

def run(player, screen):
  def deathcheck():
    if player.health <= 0:
      player.alive = False
      return False
    return True
  if baseM.hasWeapon(player, screen) or "bow" in player.items:
    weapons = True
  def start():
    def left():
        baseM.showText("A door shuts behind you, and you find yourself in the next room.",screen)
    def slimefight():
              if baseM.hasWeapon(player, screen): #only checks for sword-like weapons anyway
                baseM.showText("You slash the slime to pieces",screen)
                slimedestroyed = True
              elif "bow" in player.items:
                baseM.showText("You sink five arrows into the slime, until it finally dissolves into a puddle of goo.",screen)
                slimedestroyed = True
              else:
                baseM.showText("You have nothing to fight the slime except your bare fists. Run away or fight?",screen)
                decision4 = baseM.showText("[run, fight]",screen)
                if decision4 == "run":
                  leave()
                elif decision4 == "fight":
                  baseM.showText("You lose three more health, but manage to destroy the slime.",screen)
                  player.health -= 3
                  deathcheck()
                  slimedestroyed = True
              if slimedestroyed:
                baseM.showText("Having destroyed the slime, you open up the chest and find a sword, a shield, and 50 gold pieces.",screen)
                player.gold += 50
                player.items.append(itemStats.sword())
                player.items.append(itemStats.shield())
                baseM.showText("You see a door leading out of the room. Go through it, or go back up the staircase?",screen)
                decision5 = baseM.showText("[door, staircase]",screen)
                if decision5 == "door":
                  baseM.showText("You exit the room",screen)
                if decision5 == "staircase":
                  baseM.showText("You go back up the stairs, and you take the left passageway",screen)
                  left()
    def grab():
      baseM.showText("The torch is stuck to the wall, but by pulling on it, you shift it down, and a secret door opens in the wall to the left. Do you enter the secret door or go another way?",screen)
      decision2 = baseM.showText("[secret, another]",screen)
      if decision2 == "secret":
        baseM.showText("You find a magical breastplate that dimly glows purple in a stone relief on the wall. Putting it on increases your health by 10. You re-enter the main room.",screen)
        player.items.append(itemStats.magicalBreastplate())
        player.health += 10
        leave()
      elif decision2 == "another":
        leave()
    def leave():
      baseM.showText("Do you take the passageway on the left that is lit by torches or go down the dark staircase on the right?",screen)
      decision2 = baseM.showText("[left, right]",screen)
      if decision2 == "left":
        left()
      elif decision2 == "right":
        if itemStats.torch() in player.items:
          slimedestroyed = False
          baseM.showText("You walk down the staircase, to see a room covered with slimy goo dimly illuminated by your burning torch. In the middle of the room there is a single wooden chest. Go towards the chest, or poke the goo?:",screen)
          decision3 = baseM.showText("[go, poke]",screen)
          if decision3 == "go":
            baseM.showText("Once you reach the chest, all of the slime on the walls and the floor begin to converge, eventually surrounding and suffocating you. In the following struggle you lose 4 health, but manage to escape the slime",screen)
            player.health -= 4
            if deathcheck():
              slimefight()
          elif decision3 == "poke":
            baseM.showText("The goo converges in front of you, into a slimy mass, and lurches forward to attack you.",screen)
            slimefight()

        else:
          baseM.showText("You start down the staircase, but can't see anything, and are forced to go back up.",screen)
          start()
  


    baseM.showText("You enter the room, and see a torch burning on the wall revealing a straight passageway on the left, and a staircase leading down on the right. Do you grab the torch?",screen)
    decision1 = baseM.showText("[grab, leave]",screen)
    if decision1 == "grab":
      grab()
    elif decision1 == "leave":
      leave()
  start()




#run(player())






