"""
Author: Leon Burghardt
Created on: 2023-02-12

This is the triggerbot module.

"""

import time
import pymem.exception

from utils.offsets import get_offset
from utils.process import get_pm, get_client
from utils.config import getConfiguration

# Offsets
dwEntityList = get_offset("dwEntityList")
dwForceAttack = get_offset("dwForceAttack")
dwLocalPlayer = get_offset("dwLocalPlayer")
m_iCrosshairId = get_offset("m_iCrosshairId")
m_iTeamNum = get_offset("m_iTeamNum")
m_fFlags = get_offset("m_fFlags")


def triggerbot():
    """
    Automates the trigger process by checking if the crosshair is on an enemy player, and if so, triggers the weapon.
    """
    # get mem address of local player
    pm = get_pm()
    client = get_client()

    # main loop
    while True:
        # get local player
        local_player = pm.read_int(client + dwLocalPlayer)
        if not local_player:
            continue
        # get crosshair id
        crosshairID = pm.read_int(local_player + m_iCrosshairId)
        # get crosshair entity
        getTeam = pm.read_int(client + dwEntityList + (crosshairID - 1) * 0x10)
        if not getTeam:
            continue
        # get local player team
        localTeam = pm.read_int(local_player + m_iTeamNum)
        # get crosshair team
        try:
            crosshairTeam = pm.read_int(getTeam + m_iTeamNum)
        except pymem.exception.MemoryReadError:
            continue

        # check if crosshair is on enemy
        if crosshairID > 0 and crosshairID <= 32 and localTeam != crosshairTeam:
            # trigger
            pm.write_int(client + dwForceAttack, 6)
            # wait for delay
            time.sleep(float(getConfiguration('triggerbot+delay')))
            
