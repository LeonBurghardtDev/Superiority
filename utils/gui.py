"""
Author: Leon Burghardt
Created on: 2023-02-12

This is the GUI of the Superiority cheat, it provides a visual interface for the user to interact with the cheat.

"""

import tkinter as tk
import sys
import webbrowser
from utils.config import getConfiguration, setConfiguration
from utils.threads import bhop_change_status, esp_change_status, fov_change_status, triggerbot_change_status

class SuperiorityGUI:
    """
    This class creates the Superiority GUI.
    It consists of checkbuttons for the various cheats,
    entry widgets for inputting the triggerbot delay,
    and a link to the GitHub repository.
    """

    def __init__(self, master):
        # create the gui
        self.master = master
        # set the title of the window
        master.title("Superiority")

        # create the variables for the checkbuttons
        self.bhop_var = tk.BooleanVar()
        self.esp_var = tk.BooleanVar()
        self.fov_var = tk.BooleanVar()
        self.triggerbot_var = tk.BooleanVar()

        # set the checkbuttons to the current status of the cheats
        self.triggerbot_var.set(getConfiguration("triggerbot+toggle"))
        self.bhop_var.set(getConfiguration("bhop+toggle"))
        self.esp_var.set(getConfiguration("esp+toggle"))
        self.fov_var.set(getConfiguration("fov+toggle"))

        # create the gui elements

        # title
        self.title_label = tk.Label(master, text="Superiority v0.1 by tr3x")
        self.title_label.pack()

        # checkbutton for triggerbot
        self.triggerbot_cb = tk.Checkbutton(master, text="Triggerbot", variable=self.triggerbot_var, command=self.triggerbot_toggle)
        self.triggerbot_cb.pack()

        # input widget for triggerbot delay
        self.delay_input = tk.Entry(master)
        self.delay_input.bind("<KeyRelease>", self.on_edit)
        self.delay_input.insert(0, str(float(getConfiguration("triggerbot+delay"))*1000)+" ms")
        self.delay_input.pack()

        # checkbuttons for bhopping
        self.bhop_cb = tk.Checkbutton(master, text="Bhop", variable=self.bhop_var, command=self.bhop_toggle)
        self.bhop_cb.pack()

        # checkbuttons for esp
        self.esp_cb = tk.Checkbutton(master, text="ESP", variable=self.esp_var, command=self.esp_toggle)
        self.esp_cb.pack()

        # checkbuttons for fov
        self.fov_cb = tk.Checkbutton(master, text="FOV", variable=self.fov_var, command=self.fov_toggle)
        self.fov_cb.pack()

        # image with github logo which link to https://github.com/tr3xxx/Superiority
        self.github_logo = tk.PhotoImage(file="assets/github.png",height=114,width=114)
        self.github_link = tk.Label(master, image=self.github_logo, cursor="hand2")
        self.github_link.pack()
        self.github_link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/tr3xxx/Superiority"))

    # function for the input widget
    def on_edit(self,event):
        # Get the current value of the Entry widget
        value = self.delay_input.get()
        if not "ms" in value:
            value = value+" ms"
        value = value.replace(" ms", "")
        try:
            float(value)
            # Set the value of the input widget to the new value
            setConfiguration("triggerbot+delay", str(float(value)/1000))
        except ValueError:
            self.delay_input.delete(0, tk.END)
            self.delay_input.insert(0, str(float(getConfiguration("triggerbot+delay"))*1000)+" ms")

    # functions for the checkbuttons

    # set the configuration to the current status of the checkbutton
    def triggerbot_toggle(self):
        setConfiguration("triggerbot+toggle", str(self.triggerbot_var.get()))
        triggerbot_change_status()

    # set the configuration to the current status of the checkbutton
    def bhop_toggle(self):
        setConfiguration("bhop+toggle", str(self.bhop_var.get()))
        bhop_change_status()

    # set the configuration to the current status of the checkbutton
    def esp_toggle(self):
        setConfiguration("esp+toggle", str(self.esp_var.get()))
        esp_change_status()

    # set the configuration to the current status of the checkbutton
    def fov_toggle(self):
        setConfiguration("fov+toggle", str(self.fov_var.get()))
        fov_change_status()

# function for creating the gui
def create_gui():
    try:
        root = tk.Tk()
        root.geometry("300x300")
        root.iconbitmap("assets/icon.ico")
        root.wm_iconbitmap("assets/icon.ico")
        superiority_gui = SuperiorityGUI(root)
        root.mainloop()
        root.protocol("WM_DELETE_WINDOW", sys.exit(0))
    except Exception:
        raise("Error while creating the GUI")
