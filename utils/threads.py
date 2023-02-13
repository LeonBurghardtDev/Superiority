"""
Author: Leon Burghardt
Created on: 2023-02-11

This module contains the threads of the cheat and manages them whether they are enabled or disabled.

"""

from multiprocessing import Process

# imports of trhe cheats elements and utils
from utils.config import getConfiguration
from utils.output import print_success, print_error, print_warning
from src.bhop import bhop
from src.radar import radar
from src.aimbot import aimbot
from src.esp import esp
from src.skinchanger import skinChanger
from src.norecoil import norecoil
from src.noflash import noflash
from src.thirdperson import thirdperson
from src.triggerbot import triggerbot
from src.fov import fov

# TODO: this works, but threads would be more efficient and performant BUT threads could not be killed therefore processes are being used


# class to store the processes
class Processes:
    p_bhop:Process = None
    p_esp:Process = None
    p_fov:Process = None
    p_triggerbot:Process = None
    p_thirdperson:Process = None
    p_aimbot:Process = None
    p_radar:Process = None
    p_noflash:Process = None
    p_norecoil:Process = None
    p_skinchanger:Process = None

def bhop_change_status():
    """
    This function manages the bhop process
    """

    bhop_process = Processes.p_bhop
    if bhop_process is None:
        bhop_process = Process(target=bhop)
        Processes.p_bhop = bhop_process
    
     # create a new process for bhop
    if getConfiguration('bhop+toggle') == 'True':
        bhop_process.start()
        # check if bhop started
        if bhop_process.is_alive():
            print_success("bhop started")
        else:
            print_error("bhop failed to start")
    elif getConfiguration('bhop+toggle') == 'False':
        if bhop_process.is_alive():
            bhop_process.kill()
            Processes.p_bhop = None
        print_warning("bhop is disabled")
    else:
        print_error("bhop status could not be updated: there was an error managing the bhop process")

def esp_change_status():
    """
    This function manages the esp process
    """

    esp_process = Processes.p_esp
    if esp_process is None:
        esp_process = Process(target=esp)
        Processes.p_esp = esp_process

     # create a new process for esp
    if getConfiguration('esp+toggle') == 'True':
        esp_process.start()
        # check if esp started
        if esp_process.is_alive():
            print_success("esp started")
        else:
            print_error("esp failed to start")
    elif getConfiguration('esp+toggle') == 'False':
        if esp_process.is_alive():
            esp_process.kill()
            Processes.p_esp = None
        print_warning("esp is disabled")
    else:
        print_error("esp status could not be updated: there was an error managing the esp process")

def fov_change_status():
    """
    This function manages the fov process
    """

    fov_process = Processes.p_fov
    if fov_process is None:
        fov_process = Process(target=fov)
        Processes.p_fov = fov_process


     # create a new process for fov
    if getConfiguration('fov+toggle') == 'True':
        fov_process.start()
        # check if fov started
        if fov_process.is_alive():
            print_success("fov started")
        else:
            print_error("fov failed to start")
    elif getConfiguration('fov+toggle') == 'False':
        if fov_process.is_alive():
            fov_process.kill()
            Processes.p_fov = None
        print_warning("fov is disabled")
    else:
        print_error("fov status could not be updated: there was an error managing the fov process")

def triggerbot_change_status():
    """
    This function manages the triggerbot process
    """

    triggerbot_process = Processes.p_triggerbot
    if triggerbot_process is None:
        triggerbot_process = Process(target=triggerbot)
        Processes.p_triggerbot = triggerbot_process

     # create a new process for triggerbot
    if getConfiguration('triggerbot+toggle') == 'True':
        triggerbot_process.start()
        # check if triggerbot started
        if triggerbot_process.is_alive():
            print_success("triggerbot started")
        else:
            print_error("triggerbot failed to start")
    elif getConfiguration('triggerbot+toggle') == 'False':
        if triggerbot_process.is_alive():
            triggerbot_process.kill()
            Processes.p_triggerbot = None
        print_warning("triggerbot is disabled")
    else:
        print_error("triggerbot status could not be updated: there was an error managing the triggerbot process")


def thirdperson_change_status():
    """
    This function manages the thirdperson process
    """

    thirdperson_process = Processes.p_thirdperson
    if thirdperson_process is None:
        thirdperson_process = Process(target=thirdperson)
        Processes.p_thirdperson = thirdperson_process

     # create a new process for thirdperson
    if getConfiguration('thirdperson+toggle') == 'True':
        thirdperson_process.start()
        # check if thirdperson started
        if thirdperson_process.is_alive():
            print_success("thirdperson started")
        else:
            print_error("thirdperson failed to start")
    elif getConfiguration('thirdperson+toggle') == 'False':
        if thirdperson_process.is_alive():
            thirdperson_process.kill()
            Processes.p_thirdperson = None
        print_warning("thirdperson is disabled")
    else:
        print_error("thirdperson status could not be updated: there was an error managing the thirdperson process")

def aimbot_change_status():
    """
    This function manages the aimbot process
    """

    aimbot_process = Processes.p_aimbot
    if aimbot_process is None:
        aimbot_process = Process(target=aimbot)
        Processes.p_aimbot = aimbot_process

     # create a new process for aimbot
    if getConfiguration('aimbot+toggle') == 'True':
        aimbot_process.start()
        # check if aimbot started
        if aimbot_process.is_alive():
            print_success("aimbot started")
        else:
            print_error("aimbot failed to start")
    elif getConfiguration('aimbot+toggle') == 'False':
        if aimbot_process.is_alive():
            aimbot_process.kill()
            Processes.p_aimbot = None
        print_warning("aimbot is disabled")
    else:
        print_error("aimbot status could not be updated: there was an error managing the aimbot process")

def radar_change_status():
    """
    This function manages the radar process
    """

    radar_process = Processes.p_radar
    if radar_process is None:
        radar_process = Process(target=radar)
        Processes.p_radar = radar_process

     # create a new process for radar
    if getConfiguration('radar+toggle') == 'True':
        radar_process.start()
        # check if radar started
        if radar_process.is_alive():
            print_success("radar started")
        else:
            print_error("radar failed to start")
    elif getConfiguration('radar+toggle') == 'False':
        if radar_process.is_alive():
            radar_process.kill()
            Processes.p_radar = None
        print_warning("radar is disabled")
    else:
        print_error("radar status could not be updated: there was an error managing the radar process")

def noflash_change_status():
    """
    This function manages the noflash process
    """

    noflash_process = Processes.p_noflash
    if noflash_process is None:
        noflash_process = Process(target=noflash)
        Processes.p_noflash = noflash_process

     # create a new process for noflash
    if getConfiguration('noflash+toggle') == 'True':
        noflash_process.start()
        # check if noflash started
        if noflash_process.is_alive():
            print_success("noflash started")
        else:
            print_error("noflash failed to start")
    elif getConfiguration('noflash+toggle') == 'False':
        if noflash_process.is_alive():
            noflash_process.kill()
            Processes.p_noflash = None
        print_warning("noflash is disabled")
    else:
        print_error("noflash status could not be updated: there was an error managing the noflash process")

def norecoil_change_status():
    """
    This function manages the norecoil process
    """

    norecoil_process = Processes.p_norecoil
    if norecoil_process is None:
        norecoil_process = Process(target=norecoil)
        Processes.p_norecoil = norecoil_process

     # create a new process for norecoil
    if getConfiguration('norecoil+toggle') == 'True':
        norecoil_process.start()
        # check if norecoil started
        if norecoil_process.is_alive():
            print_success("norecoil started")
        else:
            print_error("norecoil failed to start")
    elif getConfiguration('norecoil+toggle') == 'False':
        if norecoil_process.is_alive():
            norecoil_process.kill()
            Processes.p_norecoil = None
        print_warning("norecoil is disabled")
    else:
        print_error("norecoil status could not be updated: there was an error managing the norecoil process")

def skinchanger_change_status():
    """
    This function manages the skinchanger process
    """

    skinchanger_process = Processes.p_skinchanger
    if skinchanger_process is None:
        skinchanger_process = Process(target=skinChanger)
        Processes.p_skinchanger = skinchanger_process

     # create a new process for skinchanger
    if getConfiguration('skinchanger+toggle') == 'True':
        skinchanger_process.start()
        # check if skinchanger started
        if skinchanger_process.is_alive():
            print_success("skinchanger started")
        else:
            print_error("skinchanger failed to start")
    elif getConfiguration('skinchanger+toggle') == 'False':
        if skinchanger_process.is_alive():
            skinchanger_process.kill()
            Processes.p_skinchanger = None
        print_warning("skinchanger is disabled")
    else:
        print_error("skinchanger status could not be updated: there was an error managing the skinchanger process")

def start_threads():
    """
    Starts all the threads of the cheat.
    """

    triggerbot_change_status()
    bhop_change_status()
    esp_change_status()
    aimbot_change_status()
    fov_change_status()
    radar_change_status()
    noflash_change_status()
    norecoil_change_status


