"""
Author: Leon Burghardt
Created on: 2023-02-11

This module contains the bhop function.

"""

import time
import keyboard
import pymem.exception
from utils.offsets import get_offset
from utils.process import get_pm, get_client
from utils.config import getConfiguration, setConfiguration


# Offsets
dwLocalPlayer = get_offset("dwLocalPlayer")
dwForceJump = get_offset("dwForceJump")
m_iHealth = get_offset("m_iHealth")
m_fFlags = get_offset("m_fFlags")

def bhop() -> None:
    """
    This function is a basic implementation of a bhop (bunny hop) script.

    It utilizes the pymem library to read and write memory addresses associated with the game, as well as the win32api library
    to check if the spacebar key is being pressed.
    The script runs in an infinite loop and performs a bunny hop only if the player is alive and the spacebar is being pressed.

    """

    # get process and mem adress of client
    pm = get_pm()
    client = get_client()

    # main loop
    i = 0
    while True:

        # sleep 10 milliseconds to reduce cpu usage
        time.sleep(0.01)

        # config data
        key = getConfiguration("bhop+key")

        # mouse not supported yet so we use spacebar if user enters mouse or invalid key
        try:
            keyboard.is_pressed(key)
        except:
            key = "space"
            setConfiguration("bhop+key", key) # avoid error on next loop

        try:
            # check if spacebar is being pressed
            if not keyboard.is_pressed(key):
                continue

            # get mem address of local player
            local_player: int = pm.read_int(client + dwLocalPlayer)

            # check if the address was found
            if not local_player:
                continue

            # check if player is on ground
            if pm.read_int(local_player + m_fFlags) & 1 << 0:
                # perform bunny hop
                pm.write_int(client + dwForceJump, 5)
                time.sleep(0.01)
                pm.write_int(client + m_fFlags, 4)

        except pymem.exception.MemoryReadError:
            continue

