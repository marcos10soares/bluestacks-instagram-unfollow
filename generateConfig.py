#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
import time
import sys
from pynput import keyboard
import pynput
import json

positionArray = []
countPosition = 0

centerPosition = []
backPosition = []
followsPosition = []

def generateFile():
	newPosArray = []
	count = 0
	for i in positionArray:
		newPosArray.insert(count, i[1])
		count += 1

	data = {
	"xpos": positionArray[0][0],
	"ypos": newPosArray,
	"centerPos": centerPosition,
	"backPos": backPosition,
	"followsPos": followsPosition
	}
	with open('config-new.json', 'w+') as outfile:
		json.dump(data, outfile)

def on_press(key):
	global countPosition, countPosition, centerPosition, backPosition, followsPosition
	if key == pynput.keyboard.Key.shift:
		if countPosition < 15:
			positionArray.insert(countPosition, pyautogui.position())
			print countPosition + 1
		if countPosition == 15:
			print "Press shift to view positions"
		if countPosition == 16:
			print positionArray
			print "Click on one unfollow, hover the mouse above the unfollow button on the center of the screen and press SHIFT"
		if countPosition == 17:
			print "Click cancel, hover the mouse above the BACK button and press SHIFT"
			centerPosition = pyautogui.position()
		if countPosition == 18:
			print "Click the BACK button, hover the mouse above the FOLLOWS button and press SHIFT"			
			backPosition = pyautogui.position()
		if countPosition == 19:
			print "Press SHIFT to save config file"
			followsPosition = pyautogui.position()
		if countPosition == 20:
			generateFile()
			exit()
		countPosition += 1

def generate():
	print "Hover the mouse hover each unfollow button and press SHIFT until you reach 16"
	with keyboard.Listener(on_press=on_press) as listener:
		listener.join()