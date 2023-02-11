"""
Author: Leon Burghardt
Created on: 2023-02-11

This module contains the bhop function.

"""

import pymem
import pymem.process
import time
import win32api
from utils.offsets import get_offset


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

    # get process
    pm = pymem.Pymem("csgo.exe")


    # get module address
    for module in pm.list_modules():
        if module.name == "client.dll":
            client = module.lpBaseOfDll
            break

    # main loop
    while True:

        # sleep 10 milliseconds to reduce cpu usage
        time.sleep(0.01)

        # check if spacebar is being pressed
        if not win32api.GetAsyncKeyState(0x20):
            continue

        # get mem address of local player
        local_player: int = pm.read_int(client + dwLocalPlayer)

        # check if the address was found
        if not local_player:
            continue

        # check if player is alive
        if not pm.read_int(local_player + m_fFlags):
            continue

        # check if player is on ground
        if pm.read_int(local_player + m_fFlags) & 1 << 0:
            
            # perform bunny hop
            pm.write_int(client + dwForceJump, 6)
            time.sleep(0.01)
            pm.write_int(client + m_fFlags, 4)


