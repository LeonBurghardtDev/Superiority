"""
Author: Leon Burghardt
Created on: 2023-02-12

This module is the main module of the noflash cheat.
"""


from utils.offsets import get_offset
from utils.process import get_pm, get_client

# offsets
m_flFlashMaxAlpha = get_offset("m_flFlashMaxAlpha")
dwLocalPlayer = get_offset("dwLocalPlayer")

def noflash():
    """
    This function is the noflash hack, it disables the flash effect, by setting the flash value to zero, when the player is flashed.
    """

    # get process memory and client
    pm = get_pm()
    client = get_client()

    # get local player
    local_player = pm.read_uint(client + dwLocalPlayer)

    # main loop
    while True:
        flash_value = pm.read_float(local_player + m_flFlashMaxAlpha) # get flash value
        if flash_value > 0: # if the player is flashed
            pm.write_float(local_player + m_flFlashMaxAlpha, float(0)) # set flash value to zero
