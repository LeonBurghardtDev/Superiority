"""
Author: Leon Burghardt
Created: 2023-02-12

This module contains the code for the third person changer.
"""

import keyboard
import time
import pymem.exception
from utils.offsets import get_offset
from utils.config import getConfiguration
from utils.process import get_pm,get_client

# Offsets
m_iObserverMode = get_offset("m_iObserverMode")
dwLocalPlayer = get_offset("dwLocalPlayer")



# TODO: this code works, but the perspective is not changed correctly, it is not in the back of the player if the player is moving
def thirdperson():
    """
    Function to modify the players perspective when a specific key is pressed.
    """
    print("thirdperson started")
    switch = 0 # variable for switching between the two modes

    pm = get_pm()
    client = get_client() 

    # main loop
    while True:
        # Config data
        key = getConfiguration("thirdperson+key")


        try:
            # get mem address of local player
            local_player: int = pm.read_int(client + dwLocalPlayer)

            # check if the address was found
            if not local_player:
                continue

            # check if key which has been set for third person in the config has benn pressed
            if keyboard.is_pressed(key):
                if switch == 0: # if the switch is 0, the player is in first person mode
                    pm.write_int(local_player + m_iObserverMode, 1) # change to third person mode
                    switch = 1 # change the switch to 1
                else: # if the switch is 1, the player is in third person mode
                    pm.write_int(local_player + m_iObserverMode, 0) # change to first person mode
                    switch = 0  # change the switch to 0
                time.sleep(0.1) # wait 0.1 seconds
        except pymem.exception.MemoryReadError:
            continue

