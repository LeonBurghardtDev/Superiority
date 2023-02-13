"""
Author: Leon Burghardt
Created: 2023-02-11

This module contains the code for the process class.
"""

import pymem
import pymem.process
import struct
import sys

class Process:
    """
    A class to store static variables related to the csgo process.
    """
    static_pm: pymem.Pymem = None
    static_client: __module__ = None
    static_engine: __module__ = None


def get_pm() -> pymem.Pymem:
    """
    This function checks if pm has been set and returns it if it has.
    If it hasn't, it creates a new pymem.Pymem object of the process
    of csgo

    Returns:
        pymem.Pymem: A pymem.Pymem object.

    """
    if Process.static_pm is None:
        try:
            Process.static_pm = pymem.Pymem("csgo.exe")
        except pymem.exception.ProcessNotFound:
            sys.exit("CSGO is not running!")
    return Process.static_pm

def get_client() -> int:
    """
    This function returns the client.dll module address.

    Returns:
        int: The client.dll module address.

    """
    
    if Process.static_pm is None:
        get_pm()
    if Process.static_client is None:
        for module in Process.static_pm.list_modules():
            if module.name == "client.dll":
                Process.static_client = module.lpBaseOfDll
    return Process.static_client

def get_engine() -> int:
    """
    This function returns the engine.dll module address.

    Returns:
        int: The engine.dll module address.

    """
    if Process.static_pm is None:
        get_pm()
    if Process.static_engine is None:
        for module in Process.static_pm.list_modules():
            if module.name == "engine.dll":
                Process.static_engine = module.lpBaseOfDll
    return Process.static_engine

def read_formatted_array(process: pymem.Pymem, address: int, format_string: str) -> tuple:
    size = struct.calcsize(format_string)
    raw = process.read_bytes(address, size)
    return struct.unpack(format_string, raw)