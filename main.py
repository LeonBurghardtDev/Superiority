"""
Author: Leon Burghardt
Created on: 2023-02-11

This module is the main module of the cheat.
It calls all the processes and threads -> Cheat Elements (bhop, esp, etc.)

"""
from utils.gui import create_gui
from utils.output import print_success, print_error
from multiprocessing import Process
from utils.threads import start_threads


def main():
    print_success("Superiority starting...")
    createGUI()
    start_threads()

def createGUI():
    # start gui
    gui_process = Process(target=create_gui)
    gui_process.start()

    # check if gui started
    if gui_process.is_alive():
        print_success("gui started")
    else:
        print_error("gui failed to start")
    
# entry point
if __name__ == "__main__":
    main()

    
