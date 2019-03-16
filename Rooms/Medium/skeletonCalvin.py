import random, sys
sys.path.insert(0, 'dependencies')
import baseM, itemStats

def run(player, screen):
  def grope():
        a = random.randrange(1,3)
        if a == 1:
          baseM.showText("As you grope through the darkness, your foot slips, and you fall to your death.",screen)
          player.health = 0
          player.alive = False
        elif a == 2:
          baseM.showText("You make it to the doorway and escape the room",screen)
        else:
          baseM.showText("error with a; a = %s" %a,screen)

  def stand():
        a = random.randrange(1,3)
        if a == 1:
          baseM.showText("While standing in the darkness you are attacked by something, and lose four health in the ensuing fight, but manage to escape the room afterwards",screen)
          player.health -= 4
          if player.health == 0:
            gameover()
        elif a == 2:
          baseM.showText("Nothing happens",screen)
          decision3 = baseM.showText("[grope, stand]",screen)
          if decision3 == "grope":
            grope()
          elif decision3 == "stand":
            stand()
  if baseM.hasWeapon(player, screen) or "bow" in player.items:
      weapons = True
  if itemStats.torch() in player.items:
      baseM.showText("The passageway collapses behind you, but you pull out your torch, and see something metal glinting in the darkness. Do you go towards it, or another direction?",screen)
      decision2 = baseM.showText("[metal, another]",screen)
      if decision2 == "metal":
        if "shield" in player.items:
          baseM.showText("You find a skeleton holding a shield who tries to punch you, but who you blocks with your shield",screen)
        baseM.showText("You find a skeleton holding a shield; he punches you in the face",screen)
        player.health -= 1
        if player.health == 0:
          gameover()
        elif weapons:
          baseM.showText("You destroy the skeleton, and you steal his shield",screen)
          player.items.append("shield")
      else:
        player.gold += 25
        player.items.append("magic-scroll")
        baseM.showText("You find 25 gold pieces lying on the ground, and a magic scroll",screen)

  else: 
      baseM.showText("The doorway closes behind you, leaving you in complete darkness. Do you want to grope your way through the darkness, or stand still?",screen)
      decision2 = baseM.showText("[grope, stand]",screen)

      if decision2 == "grope":
        grope()

      elif decision2 == "stand":
        stand()






