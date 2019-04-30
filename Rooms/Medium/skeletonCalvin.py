import random, sys
sys.path.insert(0, 'dependencies')
import baseM, itemStats

class Skeleton(baseM.basicEnemy):
    def __init__(self):
        self.type = "Skeleton"
        self.baseDamage = 14
        self.baseDef = 2
        self.block = 1
        self.health = 25
        self.maxHp = 25
        self.loot = [("Gold", 13), ("itemStats.shield()")]
        self.options = {"Punch":2, "Heckle":0}

def run(player):
  def grope():
        a = random.randrange(1,3)
        if a == 1:
          print("As you grope through the darkness, your foot slips, and you fall to your death.")
          player.health = 0
          player.alive = False
        elif a == 2:
          print("You make it to the doorway and escape the room")
        else:
          print("error with a; a = %s" %a)

  def stand():
        a = random.randrange(1,3)
        if a == 1:
          print("While standing in the darkness you are hit in the face by something, knocking you to the ground.")
          print("You scramble to your feet, and manage to escape the room")
          print("You lose 8 health")
          player.health -= 8
          if player.health == 0:
            gameover()
        elif a == 2:
          print("Nothing happens")
          decision3 = input("grope or stand:")
          if decision3 == "grope":
            grope()
          elif decision3 == "stand":
            stand()
  if baseM.hasWeapon(player) or "bow" in player.items:
      weapons = True
  if itemStats.torch() in player.items:
      print("The passageway collapses behind you, but you pull out your torch, and see something metal glinting in the darkness. Do you go towards it, or another direction?")
      decision2 = input("metal or another:")
      if decision2 == "metal":
        baseM.runBasicFight(player, [Skeleton()], playerFirst=False)
      elif decision2 == "another":
        player.gold += 25
        player.items.append("itemStats.fireball()")
        print("You find 25 gold pieces lying on the ground, and a scroll that imbues you with the ability to cast a fireball")

  else: 
      print("The doorway closes behind you, leaving you in complete darkness. Do you want to grope your way through the darkness, or stand still?")
      decision2 = input("grope or stand:")

      if decision2 == "grope":
        grope()

      elif decision2 == "stand":
        stand()
