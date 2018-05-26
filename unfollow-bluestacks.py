#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
import time
import sys
import json

import generateConfig

global unfollowCount
unfollowCount = 0


#check yours and update below, use positionCheck=1 to find the right positions

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




xposition = 0
positionArray = []
centerPosition = []
backPosition = []
followsPosition = []

data = {}


def readConfig():
	global xposition, positionArray, centerPosition, backPosition, followsPosition, data
	with open('config.json') as f:
		data = json.load(f)
	xposition = int(data['xpos'])
	positionArray = data['ypos']
	centerPosition = data['centerPos']
	backPosition = data['backPos']
	followsPosition = data['followsPos']


def click():
	pyautogui.mouseDown();
	time.sleep(0.5)
	pyautogui.mouseUp();

def unfollowPos(pos, delay):
	#click unfollow button, update with the right X of your screen
	pyautogui.moveTo(xposition, pos, duration=0.5)
	time.sleep(.5)
	click()

	#confirm unfollow button, update with the right X and Y of your screen
	pyautogui.moveTo(int(centerPosition[0]), int(centerPosition[1]), duration=0.5)
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
	pyautogui.moveTo(int(backPosition[0]), int(backPosition[1]), duration=0.5)
	time.sleep(2)
	click()
	#click follows button, update with the right X and Y of your screen
	pyautogui.moveTo(int(followsPosition[0]), int(followsPosition[1]), duration=0.5)
	time.sleep(2)
	click()
	time.sleep(4)

def unfollowRoutine():
	for pos in positionArray:
		unfollowPos(int(pos),timeDelay)

def Main():
	#### Start Program
	#start delay
	time.sleep(startDelay)

	if(positionCheck):
		generateConfig.generate()
		#printMousePosition()
	else:
		readConfig()
		for i in range (loops):
			print "%d loop:" % i
			unfollowRoutine()
			restart()
			time.sleep(loopSleep)

Main()