"""
Author: Leon Burghardt
Created on: 2023-02-12

This module is the main module of the radar cheat.
"""
from utils.process import get_client,get_pm
from utils.offsets import get_offset
import pymem.exception

# offsets
dwEntityList = get_offset("dwEntityList")
m_bSpotted = get_offset("m_bSpotted")


def radar():
    """
    This function is the radar hack, it shows all players on the radar by simulating them being spotted.
    """

    # get process memory and client
    pm = get_pm()
    client = get_client()

    # main loop
    while True: 
        for i in range(1, 32): # loop through all players (enteties 1-32 are reserved for players )
            entity = pm.read_int(client + dwEntityList + i * 0x10) # get entity address
            if entity:
                try:
                    pm.write_int(entity + m_bSpotted, 1) # write 1 to m_bSpotted to make the player visible on the radar
                except pymem.exception.MemoryWriteError:
                    pass