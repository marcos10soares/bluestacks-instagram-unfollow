#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
import time
import sys

global unfollowCount
unfollowCount = 0


#check yours and update below, use positionCheck=1 to find the right positions

#X Y positions

#First unfollow position
#807 201

#button to confirm unfollow
#692 448

#back button position
#458 98

#follows button position 
#769 136


#### CONFIG VARIABLES ####

#Use 1 if you want to check button positions to config program
positionCheck = 0

#Number of loops until program stops
loops = 20

#Number of seconds you need to click on bluestacks window
startDelay = 3

#Delay in seconds between each unfollow
timeDelay = 0 # should be 30

#Delay in seconds between loops
loopSleep = 5 #should be 30, use at your own risk

#Y Position of the first 16 unfollow buttons
positionArray = [201,230,256,280,304,328,359,380,404,428,459,480,506,531,559,580]



#Show mouse current position
def printMousePosition():
	print('Press Ctrl-C to quit.')
	try:
	    while True:
	        x, y = pyautogui.position()
	        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
	        print positionStr,
	        print '\b' * (len(positionStr) + 2),
	        sys.stdout.flush()
	except KeyboardInterrupt:
	    print '\n'


def click():
	pyautogui.mouseDown();
	time.sleep(0.5)
	pyautogui.mouseUp();

def unfollowPos(pos, delay):
	#click unfollow button, update with the right X of your screen
	pyautogui.moveTo(807, pos, duration=0.5)
	time.sleep(.5)
	click()

	#confirm unfollow button, update with the right X and Y of your screen
	pyautogui.moveTo(692, 448, duration=0.5)
	time.sleep(.5)
	click()

	#update count
	global unfollowCount
	unfollowCount+=1
	print "count %d" %unfollowCount
	time.sleep(delay)
	time.sleep(.5)

def restart():
	#click back button, update with the right X and Y of your screen
	pyautogui.moveTo(458, 98, duration=0.5)
	time.sleep(2)
	click()
	#click follows button, update with the right X and Y of your screen
	pyautogui.moveTo(769, 136, duration=0.5)
	time.sleep(2)
	click()
	time.sleep(4)

def unfollowRoutine():
	for pos in positionArray:
		unfollowPos(pos,timeDelay)

def Main():
	#### Start Program
	#start delay
	time.sleep(startDelay)

	if(positionCheck):
		printMousePosition()
	else:
		for i in range (loops):
			print "%d loop:" % i
			unfollowRoutine()
			restart()
			time.sleep(loopSleep)

Main()