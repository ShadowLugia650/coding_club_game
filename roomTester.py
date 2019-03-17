#This is a program that allows programmers to run thier rooms,
#without monkeying around in Main.py. here, I am importing MoneyGremlim,
#but feel free to import any room you want to test :)

import sys, random

sys.path.insert(0, 'dependencies')
import console, pScript, baseM, itemStats, artAssetsM

sys.path.insert(0, 'Rooms/Easy')
#import shopM, battleZombomanM, bestRoomRC, GobolinRC, goldenTreeM

sys.path.insert(0, 'Rooms/Medium')
#import strangerJGv1, battleGhoulM, mirrorsM, lavaroomRCv1, skeletonCalvin, reverseRoomAT, jabberwockyJG, randomMediumBattlesM, slimeroomCalvin

sys.path.insert(0, 'Rooms/Hard')
#import owM, Collector, demonicWarrior
#make sure to import the room you want to test!

sys.path.insert(0, 'Rooms/Impossible')
#import TimeEater


test =  # Change this to be whatever room you want to test
screen = artAssetsM.initScreen()
player = pScript.PChar()
test.run(player, screen)

if player.alive == False:
    print("You have died.")
else:
    print("This simulation has been TERMINATED.")















