"""
Author: Leon Burghardt
Created: 2023-02-12

This module contains the code for the aimbot.
"""

import keyboard
import math
import ast
from math import sqrt, pi, atan, asin

from utils.offsets import get_offset
from utils.process import get_pm, get_client, get_engine
from utils.config import getConfiguration


# Offsets
dwLocalPlayer = get_offset("dwLocalPlayer")
dwEntityList = get_offset("dwEntityList")
dwClientState = get_offset("dwClientState")
dwClientState_ViewAngles = get_offset("dwClientState_ViewAngles")
m_vecOrigin = get_offset("m_vecOrigin")
m_iTeamNum = get_offset("m_iTeamNum")
m_iHealth = get_offset("m_iHealth")
m_bDormant = get_offset("m_bDormant")
m_vecViewOffset = get_offset("m_vecViewOffset")
m_dwBoneMatrix = get_offset("m_dwBoneMatrix")



def normalizeAngles(viewAngelX, viewAngelY):
    """
    Normalize the angles of the view.
    
    Parameters:
    viewAngelX (float): the x angle of the view
    viewAngelY (float): the y angle of the view
    
    Returns:
    tuple: the normalized x and y angles of the view
    """
    if viewAngelX > 89:
        viewAngelX -= 360
    if viewAngelX < -89:
        viewAngelX += 360
    if viewAngelY > 180:
        viewAngelY -= 360
    if viewAngelY < -180:
        viewAngelY += 360
    return viewAngelX, viewAngelY
    
def checkAngles(x,y):
    """
    Check if the angles are within the specified range.
    
    Parameters:
    x (float): the x angle of the view
    y (float): the y angle of the view
    
    Returns:
    bool: True if the angles are within range, False otherwise
    """
    if x > 89:
        return False
    elif x < -89:
        return False
    elif y > 360:
        return False
    elif y < -360:
        return False
    else:
        return True

def nanchecker(first,second):
    """
    Check if either of the input values is NaN.
    
    Parameters:
    first (float): the first value
    second (float): the second value
    
    Returns:
    bool: True if either value is NaN, False otherwise
    """
    if math.isnan(first) or math.isnan(second):
        return True
    else:
        return False

def calc_distance(cur_x, cur_y, new_x, new_y):
    """
    Calculate the difference between two angles in the X and Y axis.

    Parameters:
        cur_x (float): Current X axis angle.
        cur_y (float): Current Y axis angle.
        new_x (float): New X axis angle.
        new_y (float): New Y axis angle.

    Returns:
        Tuple[float, float]: The difference between the two X and Y axis angles.
    """
    distance_x = new_x - cur_x # calculate the difference between the two angles
    if distance_x < -89:  
        distance_x +=  360 
    elif distance_x > 89:
        distance_x -= 360
    if distance_x < 0.0:
        distance_x = -distance_x  

    distance_y = new_y - cur_y
    if distance_y < -180:
        distance_y += 360
    elif distance_y > 180:
        distance_y -= 360
    if distance_y < 0.0:
        distance_y = -distance_y

    return distance_x, distance_y

def calcangle(localpos1, localpos2, localpos3, enemypos1, enemypos2, enemypos3):
    """
    Calculate the angle between two 3D vectors.

    Parameters:
        localpos1 (float): X coordinate of the local player.
        localpos2 (float): Y coordinate of the local player.
        localpos3 (float): Z coordinate of the local player.
        enemypos1 (float): X coordinate of the enemy player.
        enemypos2 (float): Y coordinate of the enemy player.
        enemypos3 (float): Z coordinate of the enemy player.

    Returns:
        Tuple[float, float]: The X and Y axis angles.
    """
    try:
        delta_x = localpos1 - enemypos1 
        delta_y = localpos2 - enemypos2
        delta_z = localpos3 - enemypos3
        hyp = sqrt(delta_x * delta_x + delta_y * delta_y + delta_z * delta_z)
        viewAngelX = asin(delta_z / hyp) * 57.295779513082
        viewAngelY = atan(delta_y / delta_x) * 57.295779513082
        if delta_x >= 0.0:
            viewAngelY += 180.0
        return viewAngelX, viewAngelY
    except:
        print("Error in calcangle")


def aimbot():
    """
    Main function to execute the aimbot.

    This function continuously scans the game entities and selects the closest one within the field of view. It then aims at the target.
    """

    # get process manager, client and engine
    pm = get_pm()
    client = get_client()
    engine = get_engine()

    # config data
    key = getConfiguration("aimbot+key")
    fov = int(getConfiguration("aimbot+fov"))

    # get local player
    local_player = pm.read_uint(client + dwLocalPlayer)
    engine_pointer = pm.read_uint(engine + dwClientState)
    local_player_team = pm.read_uint(local_player + m_iTeamNum)

    

    # main loop
    while True:
        target = None
        olddistx  = 111111111 # just high values
        olddisty  = 111111111 

        
        for i in range(1,32): # loop through all entities (1-32 are reserved for players)
            entity = pm.read_uint(client + dwEntityList + i * 0x10) # get entity pointer
            if entity:
                try:
                    entity_team_id = pm.read_uint(entity + m_iTeamNum) # get entity team id
                    entity_health = pm.read_uint(entity + m_iHealth) # get entity health
                    entity_dormant = pm.read_uint(entity + m_bDormant) # get entity dormant state
                except:
                    pass
                
                if entity_team_id != local_player_team and entity_health > 0: # check if entity is an enemy
                    entity_bones = pm.read_uint(entity + m_dwBoneMatrix) # get entity bone matrix

                    localpos_x_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles) # get local player view angles
                    localpos_y_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4) # get local player view angles
                    localpos_z_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x8) # get local player view angles

                    localpos_x = pm.read_float(local_player + m_vecOrigin) # get local player position
                    localpos_y = pm.read_float(local_player + m_vecOrigin + 4) # get local player position
                    localpos_z = pm.read_float(local_player + m_vecOrigin + 8) + localpos_z_angles # get local player position

                    try:
                        entitypos_x = pm.read_float(entity_bones + 0x30 * 8 + 0xC) # get entity position
                        entitypos_y = pm.read_float(entity_bones + 0x30 * 8 + 0x1C) # get entity position
                        entitypos_z = pm.read_float(entity_bones + 0x30 * 8 + 0x2C) # get entity position
                    except:
                        continue

                    X, Y = calcangle(localpos_x, localpos_y, localpos_z, entitypos_x, entitypos_y, entitypos_z) # calculate angle between local player and entity
                    newdist_x, newdist_y = calc_distance(localpos_x_angles, localpos_y_angles, X, Y) # calculate distance between local player and entity

                    if newdist_x < olddistx and newdist_y < olddisty and newdist_x <= fov and newdist_y <= fov: # check if entity is closer than the previous one
                        olddistx = newdist_x # update old distance
                        olddisty = newdist_y # update old distance
                        target = entity # set target
                        target_hp = entity_health # set target hp
                        target_dormnat = entity_dormant # set target dormant state

                        target_x = entitypos_x # set target position
                        target_y = entitypos_y # set target position
                        target_z = entitypos_z # set target position
                    
                    if keyboard.is_pressed(key): # check if aimbot key is pressed
                        if target and target_hp > 0 and not target_dormnat: # check if target is valid
                            x, y = calcangle(localpos_x, localpos_y, localpos_z, target_x, target_y, target_z) # calculate angle between local player and target
                            normalize_x, normalize_y = normalizeAngles(x, y) # normalize angle
                            normalize_x = normalize_x / 180 * math.pi # if this is not here the aimbot will aim way too high
                            
                            pm.write_float(engine_pointer + dwClientState_ViewAngles, normalize_x) # write new view angles
                            pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, normalize_y) # write new view angles
                        	




