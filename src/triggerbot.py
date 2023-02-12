import time

from utils.offsets import get_offset
from utils.process import get_pm, get_client
from utils.config import getConfiguration


dwEntityList = get_offset("dwEntityList")
dwForceAttack = get_offset("dwForceAttack")
dwLocalPlayer = get_offset("dwLocalPlayer")
m_iCrosshairId = get_offset("m_iCrosshairId")
m_iTeamNum = get_offset("m_iTeamNum")
m_fFlags = get_offset("m_fFlags")


def triggerbot():
    pm = get_pm()
    client = get_client()

    while True:
        local_player = pm.read_int(client + dwLocalPlayer)
        if not local_player:
            continue
        crosshairID = pm.read_int(local_player + m_iCrosshairId)
        getTeam = pm.read_int(client + dwEntityList + (crosshairID - 1) * 0x10)
        if not getTeam:
            continue
        localTeam = pm.read_int(local_player + m_iTeamNum)
        crosshairTeam = pm.read_int(getTeam + m_iTeamNum)

        if crosshairID > 0 and crosshairID <= 32 and localTeam != crosshairTeam:
            pm.write_int(client + dwForceAttack, 6)
            time.sleep(float(getConfiguration('triggerbot+delay')))
            
