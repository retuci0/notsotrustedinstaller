"""
simple python program to run programs with trustedinstaller privileges
made by retti :3
feel free to skid

i was thinking of making a token duplication script for this but using the
parent method with a powershell script is just way easier
"""

from pyuac import main_requires_admin
import subprocess

import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import PhotoImage
from tkinter import ttk

class NSTI:
    
    @main_requires_admin
    def __init__(self):
        # root window
        self.root: tk.Tk = tk.Tk()
        self.root.title("NotSoTrustedInstaller")
        self.root.iconbitmap()
        self.root.geometry("300x70")
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)
        self.root.focus()
        
        # icon
        self.icon = PhotoImage(file="icon.png")
        self.root.iconphoto(False, self.icon)
        
        # create widgets
        self.create_widgets()
        
        # load last run command
        self.load_last_run()
        
    def create_widgets(self) -> None:
        """what do you think this does dumbass"""
        # cool asf icon
        self.icon_label = tk.Label(self.root, image=self.icon, bg="#ffffff")
        self.icon_label.place(relx=0.1, rely=0.5, anchor="center")
        
        # executable name entry
        self.name_field = ttk.Entry(self.root)
        self.name_field.place(relx=0.25,  rely=0.5, anchor="w")
        self.name_field.bind("<Return>", self.run_as_ti)
        
        # run button (duh)
        self.run_button = ttk.Button(self.root, text="run as TI", command=self.run_as_ti)
        self.run_button.place(relx=0.85, rely=0.5, anchor="center")
        
    def run_as_ti(self, event: tk.Event = None) -> None:
        """gets the executable name passed in the entry and runs it with TI privileges"""
        executable_name = self.name_field.get().strip()
        if not executable_name:
            msgbox.showerror("you fucking dipshit", "if you want to run something as TI input something you dumb fuck")
            return
    
        # save the last run command
        self.save_last_run(executable_name)
        
        # error handling (kinda)
        try:
            subprocess.Popen(["powershell", f"./ti.ps1 -executableName {executable_name}"])
        except Exception as e:
            print(e)
            msgbox.showerror("fuck", "it didn't work lmao what a skill issue")
            self.root.destroy()
    
    def save_last_run(self, command: str) -> None:
        """save the last run command to a text file"""
        with open("last_run.txt", "w") as file:
            file.write(command)
    
    def load_last_run(self) -> None:
        """load the last run command"""
        try:
            with open("last_run.txt", "r") as file:
                last_command = file.read().strip()
                self.name_field.insert(0, last_command)
        except FileNotFoundError:
            pass # context: file was not found and it raised an error
      
      
# run
if __name__ == "__main__":
    try:
        NSTI().root.mainloop()
        
    # every time i close the tk window it spits out an attributeerror so fuck it it doesn't any more
    except AttributeError:
        pass