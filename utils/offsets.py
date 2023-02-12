"""
Author: Leon Burghardt
Created on: 2023-02-11

This module contains functions for getting offsets from the hazedumper repository.

"""

import requests

def get_offset(offset: str) -> int:
    """
    This function makes a GET request to the URL "https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json" (most recent csgo offsets)
    and returns the value for the specified offset in either the "signatures" or "netvars" key in the JSON response from the server.
    
    Args:
        offset (str): The offset to search for in the JSON response.
    
    Returns:
        Any: The value associated with the specified offset in either the "signatures" or "netvars" key in the JSON response, 
        or a message indicating that the offset was not found if it is not found in either key.
    """

    response = requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json")
    data = response.json()

    try:
        return data["signatures"][offset]
    except KeyError:
        try:
            return data["netvars"][offset]
        except KeyError:
            return f"Offset {offset} not found!"


def get_all_offsets() -> dict:

    """
    This function makes a GET request to the URL "https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json" (most recent csgo offsets)
    and returns the JSON response from the server.
    
    Returns:
        dict: The JSON response from the server.
    """

    return requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json").json()
