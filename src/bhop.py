import pymem
import pymem.process
import time
import win32api


# offsets
LOCAL_PLAYER = 14316652
FORCE_JUMP = 86422944
HEALTH = 256
FLAGS = 260

def bhop() -> None:
    pm = pymem.Pymem("csgo.exe")


    # get module address
    for module in pm.list_modules():
        if module.name == "client.dll":
            client = module.lpBaseOfDll
            break

    # loop
    while True:
        # sleep
        time.sleep(0.01)

        # check if key is pressed
        if not win32api.GetAsyncKeyState(0x20):
            continue

        # get player
        local_player: int = pm.read_int(client + LOCAL_PLAYER)

        if not local_player:
            continue

        # is player alive
        if not pm.read_int(local_player + HEALTH):
            continue

        # get player flags
        if pm.read_int(local_player + FLAGS) & 1 << 0:
            # jump
            pm.write_int(client + FORCE_JUMP, 6)
            time.sleep(0.01)
            pm.write_int(client + FORCE_JUMP, 4)


