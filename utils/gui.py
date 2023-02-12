"""
Author: Leon Burghardt
Created on: 2023-02-12

This is the GUI of the Superiority cheat, it provides a visual interface for the user to interact with the cheat.

"""

import tkinter as tk
import sys
import os
import ast
import webbrowser
from utils.config import getConfiguration, setConfiguration
from utils.threads import bhop_change_status, esp_change_status, fov_change_status, triggerbot_change_status, thirdperson_change_status 


class SuperiorityGUI():
    """
    This class creates the Superiority GUI.
    It consists of checkbuttons for the various cheats,
    entry widgets for inputting the triggerbot delay,
    and a link to the GitHub repository.
    """
    triggerbot_btn_text = f"Triggerbot ({getConfiguration('triggerbot+activate+key').upper()})"
    bhop_btn_text = f"Bunnyhop ({getConfiguration('bhop+activate+key').upper()})"
    thirdperson_btn_text = f"Thirdperson ({getConfiguration('thirdperson+activate+key').upper()})"
    esp_btn_text = f"ESP ({getConfiguration('esp+activate+key').upper()})"
    fov_btn_text = f"FOV ({getConfiguration('fov+activate+key').upper()})"

    def __init__(self, master):
        # create the gui
        self.master = master
        # set the title of the window
        master.title("Superiority")

        # create the variables for the checkbuttons
        self.bhop_var = tk.BooleanVar()
        self.thirdperson_var = tk.BooleanVar()
        self.esp_var = tk.BooleanVar()
        self.fov_var = tk.BooleanVar()
        self.triggerbot_var = tk.BooleanVar()

        # set the checkbuttons to the current status of the cheats
        self.triggerbot_var.set(getConfiguration("triggerbot+toggle"))
        self.bhop_var.set(getConfiguration("bhop+toggle"))
        self.thirdperson_var.set(getConfiguration("thirdperson+toggle"))
        self.esp_var.set(getConfiguration("esp+toggle"))
        self.fov_var.set(getConfiguration("fov+toggle"))

        # create the gui elements

        # title
        self.title_label = tk.Label(master, text="Superiority v0.1 by tr3x")
        self.title_label.pack()

        # checkbutton for triggerbot
        self.triggerbot_cb = tk.Checkbutton(master,name='triggebot', text=self.triggerbot_btn_text, variable=self.triggerbot_var, command=self.triggerbot_toggle)
        self.triggerbot_cb.pack()

        
        # input widget for triggerbot delay
        self.delay_input = tk.Entry(master)
        self.delay_input.bind("<KeyRelease>", self.on_edit)
        self.delay_input.insert(0, str(float(getConfiguration("triggerbot+delay"))*1000)+" ms")
        self.delay_input.pack()

        # checkbuttons for bhopping
        self.bhop_cb = tk.Checkbutton(master,name='bhop', text=self.bhop_btn_text, variable=self.bhop_var, command=self.bhop_toggle)
        self.bhop_cb.pack()

        # checkbuttons for thirdperson
        self.thirdperson_cb = tk.Checkbutton(master,name='thirdperson', text=self.thirdperson_btn_text, variable=self.thirdperson_var, command=self.thirdperson_toggle)
        self.thirdperson_cb.pack()

        # checkbuttons for esp
        self.esp_cb = tk.Checkbutton(master,name='esp',text=self.esp_btn_text, variable=self.esp_var, command=self.esp_toggle)
        self.esp_cb.pack()

        # checkbuttons for fov
        self.fov_cb = tk.Checkbutton(master,name='fov', text=self.fov_btn_text, variable=self.fov_var, command=self.fov_toggle)
        self.fov_cb.pack()

        # button which open a file in a specified directory
        self.open_config_btn = tk.Button(master, text="Open config", command=self.open_config)
        self.open_config_btn.pack()

        # image with github logo which link to https://github.com/tr3xxx/Superiority
        self.github_logo = tk.PhotoImage(file="assets/github.png",height=114,width=114)
        self.github_link = tk.Label(master, image=self.github_logo, cursor="hand2")
        self.github_link.pack()
        self.github_link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/tr3xxx/Superiority"))

    
        self.master.after(500, self.current_checkbox_value) # update the checkbox values every 500ms


    # update checkbox value 
    def current_checkbox_value(self):
        """
        This function updates the checkbox values according to the current status of the config.
        """

        for widget in self.master.winfo_children(): # loop through all widgets in the window
            if isinstance(widget, tk.Checkbutton): # if the widget is a checkbutton
                if widget.cget("text") == self.triggerbot_btn_text: # if the checkbutton is the triggerbot checkbutton
                    if ast.literal_eval(getConfiguration("triggerbot+toggle")): # if the triggerbot is enabled in cfg
                        widget.select() # select the checkbutton
                    else: # if the triggerbot is disabled in cfg
                        widget.deselect() # deselect the checkbutton
                if widget.cget("text") == self.bhop_btn_text: # if the checkbutton is the bhop checkbutton
                    if ast.literal_eval(getConfiguration("bhop+toggle")): # if the bhop is enabled in cfg
                        widget.select() # select the checkbutton
                    else: # if the bhop is disabled in cfg
                        widget.deselect() # deselect the checkbutton
                if widget.cget("text") == self.esp_btn_text: # if the checkbutton is the esp checkbutton
                    if ast.literal_eval(getConfiguration("esp+toggle")):  # if the esp is enabled in cfg
                        widget.select() # select the checkbutton
                    else: # if the esp is disabled in cfg
                        widget.deselect() # deselect the checkbutton
                if widget.cget("text") == self.fov_btn_text: # if the checkbutton is the fov checkbutton
                    if ast.literal_eval(getConfiguration("fov+toggle")): # if the fov is enabled in cfg
                        widget.select() # select the checkbutton
                    else: # if the fov is disabled in cfg
                        widget.deselect() # deselect the checkbutton
        self.master.after(500, self.current_checkbox_value) # update the checkbox value every 500ms
                        
    # function for the input widget
    def on_edit(self):
        """
        This function is called when the user edits the input widget for the triggerbot delay.
        """

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

    def open_config(self):
        """
        This function opens the config file in the default text editor.
        """
        dir = os.path.expanduser('~/Documents')+"/Superiority/config.cfg"
        os.startfile(dir)

    # functions for the checkbuttons

    # set the configuration to the current status of the checkbutton
    def triggerbot_toggle(self):
        setConfiguration("triggerbot+toggle", str(self.triggerbot_var.get()))
        triggerbot_change_status()

    # set the configuration to the current status of the checkbutton
    def bhop_toggle(self):
        setConfiguration("bhop+toggle", str(self.bhop_var.get()))
        bhop_change_status()

    def thirdperson_toggle(self):
        setConfiguration("thirdperson+toggle", str(self.thirdperson_var.get()))
        thirdperson_change_status()

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
    """
    This function creates the gui.
    """
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
