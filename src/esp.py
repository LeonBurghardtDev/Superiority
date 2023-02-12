"""
Author: Leon Burghardt
Created on: 2023-02-11

This module is used to enable ESP (Extra Sensory Perception).

"""

from utils.offsets import get_offset
from utils.process import get_pm, get_client

# Offsets
dwEntityList = get_offset("dwEntityList")
dwGlowObjectManager = get_offset("dwGlowObjectManager")
m_iGlowIndex = get_offset("m_iGlowIndex")
m_iTeamNum = get_offset("m_iTeamNum")

def esp():
    """
    This function is the main function of the module. It uses Pymem to connect to the process of the game "csgo.exe",
    retrieves the base address of the module "client.dll",
    and then continuously loops through the entities in the game to find the Terrorist and Counter-Terrorist players.
    
    The glow color for each player is set based on their team, and the glow is enabled for each player.

    """

    # get process and mem adress of client
    pm = get_pm()
    client = get_client()

    # Loop indefinitely without sleeping to continuously update the ESP
    while True:
        # Read the address of the glow manager from memory
        glow_manager = pm.read_int(client + dwGlowObjectManager)

        # loop through player reserved entities 1-32 
        for i in range(1, 32): 

            # Read the address of the entity from memory
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                # if exist, read teamd id and glow index
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)

                if entity_team_id == 2:  # t
                    # set glow to red
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))   # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))  # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow

                elif entity_team_id == 3:  # ct
                    
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))   # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))  # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow
