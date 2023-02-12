"""
Author: Leon Burghardt
Created: 2023-02-11

This module contains the code for the fov changer.

"""
import keyboard
import time
from utils.offsets import get_offset
from utils.config import getConfiguration
from utils.output import print_success
from utils.process import get_pm, get_client


# Offsets
dwEntityList = get_offset("dwEntityList")
m_iDefaultFOV = get_offset("m_iDefaultFOV")
dwLocalPlayer = get_offset("dwLocalPlayer")
m_fFlags = get_offset("m_fFlags")

# Config data
targetFov = getConfiguration("fov")
key = getConfiguration("fov+key")


def fov():
    """
    Function to modify the field when a key is pressed.
    """
    pm = get_pm()
    client = get_client()
    
    # main loop
    while True:
        # get mem address of local player
        local_player: int = pm.read_int(client + dwLocalPlayer)

        # check if the address was found
        if not local_player:
            continue

        # check if player is alive
        if not pm.read_int(local_player + m_fFlags):
            continue

        iFOV = pm.read_int(local_player + m_iDefaultFOV)

        if keyboard.is_pressed(key):
            if iFOV == int(targetFov):
                pm.write_int(local_player + m_iDefaultFOV, 106)
                print_success(f"FOV changed from {targetFov} to 106")
            else:
                pm.write_int(local_player + m_iDefaultFOV, int(targetFov))
                print_success(f"FOV changed from 106 to {targetFov}")
            time.sleep(0.1)


