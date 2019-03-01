import random

#class player:
 # def __init__(self):
  #  self.health = 10
   # self.gold = 0
    #self.items = ["axe", "loincloth", "torch", "shield"]

def run(player):
  def deathcheck():
    if player.health <= 0:
      player.alive = False
      return False
    return True
  if "sword" in player.items or "axe" in player.items or "bow" in player.items:
    weapons = True
  def start():
    def left():
        print("A door shuts behind you, and you find yourself in the next room.")
    def slimefight():
              if "axe" or "sword" in player.items:
                print("You slash the slime to pieces")
                slimedestroyed = True
              elif "bow" in player.items:
                print("You sink five arrows into the slime, until it finally dissolves into a puddle of goo.")
                slimedestroyed = True
              else:
                print("You have nothing to fight the slime except your bare fists. Run away or fight?")
                decision4 = input("run or fight?:")
                if decision4 == "run":
                  leave()
                elif decision4 == "fight":
                  print("You lose three more health, but manage to destroy the slime.")
                  player.health -= 3
                  deathcheck()
                  slimedestroyed = True
              if slimedestroyed:
                print("Having destroyed the slime, you open up the chest and find a sword, a shield, and 50 gold pieces.")
                player.gold += 50
                player.items.append("sword")
                player.items.append("shield")
                print("You see a door leading out of the room. Go through it, or go back up the staircase?")
                decision5 = input("door or staircase:")
                if decision5 == "door":
                  print("You exit the room")
                if decision5 == "staircase":
                  print("You go back up the stairs, and you take the left passageway")
                  left()
    def grab():
      print("The torch is stuck to the wall, but by pulling on it, you shift it down, and a secret door opens in the wall to the left. Do you enter the secret door or go another way?")
      decision2 = input("secret or another?:")
      if decision2 == "secret":
        print("You find a magical breastplate that dimly glows purple in a stone relief on the wall. Putting it on increases your health by 10. You re-enter the main room.")
        player.items.append("magic-breastplate")
        player.health += 10
        leave()
      elif decision2 == "another":
        leave()
    def leave():
      print("Do you take the passageway on the left that is lit by torches or go down the dark staircase on the right?")
      decision2 = input("left or right:")
      if decision2 == "left":
        left()
      elif decision2 == "right":
        if "torch" in player.items:
          slimedestroyed = False
          print("You walk down the staircase, to see a room covered with slimy goo dimly illuminated by your burning torch. In the middle of the room there is a single wooden chest. Go towards the chest, or poke the goo?:")
          decision3 = input("go or poke:")
          if decision3 == "go":
            print("Once you reach the chest, all of the slime on the walls and the floor begin to converge, eventually surrounding and suffocating you. In the following struggle you lose 4 health, but manage to escape the slime")
            player.health -= 4
            if deathcheck():
              slimefight()
          elif decision3 == "poke":
            print("The goo converges in front of you, into a slimy mass, and lurches forward to attack you.")
            slimefight()

        else:
          print("You start down the staircase, but can't see anything, and are forced to go back up.")
          start()
  


    print("You enter the room, and see a torch burning on the wall revealing a straight passageway on the left, and a staircase leading down on the right. Do you grab the torch?")
    decision1 = input("grab or leave:")
    if decision1 == "grab":
      grab()
    elif decision1 == "leave":
      leave()
  start()




#run(player())
