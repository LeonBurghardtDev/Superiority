from utils.offsets import get_offset
from utils.process import get_pm, get_client, get_engine, read_formatted_array
import pymem
import ctypes
import pymem.process
import time

# offsets
1


# TODO: its static atm, make it dynamic
def GetWeaponPaint(itemDefinition: ctypes.c_short):
    if itemDefinition ==  1:
        return 37 # deagle
    elif itemDefinition ==  4:
        return 38 # glock
    elif itemDefinition ==  7:
        return 614 # ak47
    elif itemDefinition ==  9:
        return 344 # awp
    elif itemDefinition ==  61:
        return 653 # usp




def skinChanger():
    pm = get_pm()
    client = get_client()
    engine = get_engine()

    while True:
        time.sleep(2)
        localPlayer = pm.read_int(client + dwLocalPlayer)
        if localPlayer:
            weapons = read_formatted_array(pm, localPlayer + m_hMyWeapons,"<LLLLLLLL")

            for weapon in weapons:
                weapon = pm.read_uint((client+dwEntityList + (weapon & 0xFFF) * 0x10)-0x10)
                if weapon:
                    paint:ctypes.c_short = GetWeaponPaint(pm.read_short(weapon + m_iItemDefinitionIndex))
                    if paint:
                        print(paint, pm.read_uint(weapon + m_nFallbackPaintKit))
                        shouldUpdate:bool = pm.read_uint(weapon + m_nFallbackPaintKit) != paint
                        #print(shouldUpdate)
                        try:
                            pm.write_int(weapon+m_iItemIDHigh, -1)
                            pm.write_int(weapon+m_nFallbackPaintKit, paint)
                            pm.write_float(weapon+m_flFallbackWear, float(0.1))

                            if shouldUpdate:
                                pm.write_int(pm.read_uint(engine + dwClientState) + 0x174, -1)
                        except pymem.exception.MemoryWriteError:
                            print("MemoryWriteError")
                          