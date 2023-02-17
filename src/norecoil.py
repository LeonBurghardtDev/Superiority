from math import isnan
import pymem.exception

from utils.process import get_pm, get_client, get_engine
from utils.offsets import get_offset

# offsets

dwLocalPlayer = get_offset("dwLocalPlayer")
dwClientState = get_offset("dwClientState")
m_iShotsFired = get_offset("m_iShotsFired")
dwClientState_ViewAngles = get_offset("dwClientState_ViewAngles")
m_aimPunchAngle = get_offset("m_aimPunchAngle")

def nanchecker(first,second):
    """
    Check if either of the input values is NaN.
    
    Parameters:
    first (float): the first value
    second (float): the second value
    
    Returns:
    bool: True if either value is NaN, False otherwise
    """
    if isnan(first) or isnan(second):
        return False
    else:
        return True


def checkangles(x,y):
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


def norecoil():
    """
    This function removes the recoil from the players weapon.
    """

    pm = get_pm()
    client = get_client()
    engine = get_engine()
    try:
        engine_pointer = pm.read_uint(engine + dwClientState)

        #main loop
        while True:
            old_punch_x = 0.0
            old_punch_y = 0.0

            #get the local player
            local_player = pm.read_uint(client + dwLocalPlayer)
            if pm.read_uint(local_player + m_iShotsFired) > 2:
                rcs_x = pm.read_float(engine_pointer + dwClientState_ViewAngles)
                rcs_y = pm.read_float(engine_pointer + dwClientState_ViewAngles + 4)

                punchx = pm.read_float(local_player + m_aimPunchAngle)
                punchy = pm.read_float(local_player + m_aimPunchAngle + 4)

                newrcs_x = rcs_x - (punchx - old_punch_x) * 2
                newrcs_y = rcs_y - (punchy - old_punch_y) * 2

                old_punch_x = punchx
                old_punch_y = punchy
                print(newrcs_x,newrcs_y)

                if nanchecker(newrcs_x,newrcs_y) and checkangles(newrcs_x,newrcs_y):
                    pm.write_float(engine_pointer + dwClientState_ViewAngles, newrcs_x)
                    pm.write_float(engine_pointer + dwClientState_ViewAngles + 4, newrcs_y)
            else:
                    old_punch_x = pm.read_float(local_player + m_aimPunchAngle)
                    old_punch_y = pm.read_float(local_player + m_aimPunchAngle + 4)
                    newrcs_x = old_punch_x
                    newrcs_y = old_punch_y
    except pymem.exception.MemoryReadError:
        pass
