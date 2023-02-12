"""
Author: Leon Burghardt
Created on: 2023-02-11

This module manages the config file.

"""
from utils.output import print_success, print_error
import os
import configparser

# Path to the Superiority directory in the Documents folder
dir = os.path.expanduser('~/Documents')+"/Superiority"

def ensure_config_exists():
    """
    Ensures that the config file exists in the Superiority directory. 
    If the file does not exist, creates a new one with default values.
    """

    # Create a ConfigParser object
    config = configparser.ConfigParser()
    # Set default values for the config file
    config['DEFAULT'] = {
                            'triggerbot+toggle': 'False',
                            'triggerbot+delay': '0.1',
                            'triggerbot+activate+key': 'f1',

                            'bhop+toggle': 'False',
                            'bhop+key': 'scroll down',
                            'bhop+activate+key': 'f2',

                            'thirdperson+toggle': 'False',      
                            'thirdperson+key': 'v',
                            'thirdperson+activate+key': 'f3',

                            'esp+toggle': 'False',
                            'esp+activate+key': 'f4',

                            'radar+toggle': 'False',
                            'radar+activate+key': 'f5',

                            'norecoil+toggle': 'False',
                            'norecoil+activate+key': 'f6',

                            'noflash+toggle': 'False',
                            'noflash+activate+key': 'f7',

                            'fov+toggle': 'False',
                            'fov': '140',
                            'fov+key': 'x',
                            'fov+activate+key': 'f8',

                            'aimbot+toggle': 'False',
                            'aimbot+key': 'alt',
                            'aimbot+fov': '140',
                            'aimbot+activate+key': 'f9',

                        }

    # Check if the Superiority directory exists
    if not os.path.exists(dir):
        # Print an error message if the directory does not exist
        print_error("Config file not found")
        # Create the directory
        os.mkdir(dir)

    # Join the directory path and the config file name
    filename = os.path.join(dir, 'config.cfg')
    if not os.path.exists(filename):
        # Write the default values to the config file
        with open(filename, 'w') as configfile:
            config.write(configfile)
            # Print a success message for creating the new config file
            print_success(f"New Config file created ({dir}/config.cfg)")
    

def getConfiguration(key: str) -> str:
    """
    Returns the value of the specified key from the config file.
    If the key does not exist in the config file, raises a ValueError.
    """

    # Ensure that the config file exists
    ensure_config_exists()

    # Create a ConfigParser object
    config = configparser.ConfigParser()
    # Read the config file
    config.read(f'{dir}/config.cfg')

    try:
        # Get the value of the specified key from the config file
        key = config.get('DEFAULT', key)
        # Return the value of the key
        return key
    except ValueError:
        # Raise a ValueError if the key does not exist in the config file
        raise ValueError(f"{key} could not be found in config file")

def setConfiguration(key: str,value: any):
    """
    Sets the value of the specified key in the config file.
    If the key does not exist in the config file, raises a ValueError.
    """

    # Ensure that the config file exists
    ensure_config_exists()

    # Create a ConfigParser object
    config = configparser.ConfigParser()
    # Read the config file
    config.read(f'{dir}/config.cfg')

    try:
        # Set the value of the specified key in the config file
        config.set('DEFAULT', key, value)
        # Write the changes to the config file
        with open(f'{dir}/config.cfg', 'w') as configfile:
            config.write(configfile)
    except ValueError:
        # Raise a ValueError if the key does not exist in the config file
        raise ValueError(f"{key} could not be found in config file")
