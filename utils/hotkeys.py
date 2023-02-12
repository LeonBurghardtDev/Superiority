"""
Author: Leon Burghardt
Created on: 2023-02-12

This module manages the hotkeys of the cheat.
"""

import keyboard
import time
import ast
from utils.config import getConfiguration,setConfiguration
from utils.threads import bhop_change_status, esp_change_status, fov_change_status, triggerbot_change_status

def hotkeys_watcher():
    """
    This function watches for hotkeys and changes the status of the cheat elements in the cfg, so it will be enabeld and the gui will recognise.
    """
    while True:
        if keyboard.is_pressed(getConfiguration("triggerbot+activate+key")): # if the key which is set for activating the triggerbot in the config is pressed
            setConfiguration("triggerbot+toggle",str(not ast.literal_eval(getConfiguration("triggerbot+toggle")))) # change the status of the triggerbot in the config
            triggerbot_change_status() # activates the triggerbot and changes the status of the triggerbot in the gui
        if keyboard.is_pressed(getConfiguration("bhop+activate+key")):  # if the key which is set for activating the bhop in the config is pressed
            setConfiguration("bhop+toggle", str(not ast.literal_eval(getConfiguration("bhop+toggle")))) # change the status of the bhop in the config
            bhop_change_status() # activates the bhop and changes the status of the bhop in the gui
        if keyboard.is_pressed(getConfiguration("esp+activate+key")): # if the key which is set for activating the esp in the config is pressed
            setConfiguration("esp+toggle", str(not ast.literal_eval(getConfiguration("esp+toggle")))) # change the status of the esp in the config
            esp_change_status() # activates the esp and changes the status of the esp in the gui
        if keyboard.is_pressed(getConfiguration("fov+activate+key")): # if the key which is set for activating the fov in the config is pressed
            setConfiguration("fov+toggle", str(not ast.literal_eval(getConfiguration("fov+toggle")))) # change the status of the fov in the config
            fov_change_status() # activates the fov and changes the status of the fov in the gui
        time.sleep(0.1) # wait 0.1 seconds to reduce cpu usage