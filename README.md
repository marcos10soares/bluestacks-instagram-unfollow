# bluestacks-instagram-unfollow
Unfollow all your follows using bluestacks and instagram app

https://imgur.com/kCFEPOv

https://youtu.be/8kVrY760rYQ


**Dependencies**

pyautogui

https://pyautogui.readthedocs.io/en/latest/

```pip install pyautogui```


**Requirements**

Bluestacks

http://bluestacks.com


**Instructions**

Install bluestacks, install instagram app, login with you account and go to the follows screen.

Open ununfollow-bluestacks.py and change:

```positionCheck = 0``` to ```positionCheck = 1```

Start the program with:
```python unfollow-bluestacks.py```

(See the instructions video above to generate the config file)

Hover above each button and press LEFT SHIFT key for each step.

After generating the config.json file change:

```positionCheck = 1``` to ```positionCheck = 0```

And run the program.

Done.

**Options inside 'unfollow-bluestacks.py'**

#Use 1 to generate the config.json with the correct mouse positions for your resolution

```positionCheck = 0```

#Number of loops until program stops

```loops = 20```

#Number of seconds you need to click on bluestacks window

```startDelay = 3```

#Delay in seconds between each unfollow, use 20-30 to avoid soft bans

```timeDelay = 0```

#Delay in seconds between loops, use 20-30 to avoid soft bans

```loopSleep = 5```

