import os
import subprocess
import sys
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle

import sv_ttk

class PUBGLauncher:
    def __init__(self, master):
        self.master = master
        master.title("PUBG Launcher")
        
        self.style = ThemedStyle(master)
        self.style.set_theme("equilux")
        
        # Set window icon
        icon = Image.open(resource_path("kanalinko.png"))
        icon = ImageTk.PhotoImage(icon)
        master.iconphoto(True, icon)
        
        self.pubg_exec = ["ExecPubg.exe", "TslGame.exe", "TslGame_BE.exe", "TslGame_UC.exe", "zksvc.exe", "BEService.exe"]
        

        self.start_button = ttk.Button(master, text="Start PUBG",  width=20)
        self.start_button.pack(fill=tk.X, padx=10, pady=(10, 5))

        self.restart_button = ttk.Button(master, text="Restart PUBG",  width=20)
        self.restart_button.pack(fill=tk.X, padx=10, pady=5)
        
        self.kill_button = ttk.Button(master, text="Kill PUBG",  width=20)
        self.kill_button.pack(fill=tk.X, padx=10, pady=5)
        

        """ self.clear_cache_button = ttk.Button(master, text="Clear Cache", width=20)
        self.clear_cache_button.pack(fill=tk.X, padx=10, pady=5) """


        master.after(100, self.setup_commands)
        
    def setup_commands(self):
        # Set commands for buttons
        self.start_button.config(command=self.start_pubg)
        self.restart_button.config(command=self.restart_pubg)
        self.kill_button.config(command=self.kill_pubg)
        """ self.clear_cache_button.config(command=self.clear_cache) """
        
    def start_pubg(self):
        print("Lauching")
        try:
            os.startfile("steam://rungameid/578080")     # Search for an optional -silent flag if possible
            #subprocess.Popen("steam://rungameid/578080")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start PUBG: {str(e)}")

    def restart_pubg(self):
        print("Restarting...")
        try:
            for x in self.pubg_exec:
                os.system("TASKKILL /F /IM " + x)
            # Wait for the process to be terminated
            os.system("ping 1.1.1.1 -n 1 -w 5000 > nul")
            self.start_pubg()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to restart PUBG: {str(e)}")

        
    def kill_pubg(self):
        print("Kill")
        try:
            for x in self.pubg_exec:
                os.system("TASKKILL /F /IM " + x)
            # Wait for the process to be terminated
            os.system("ping 1.1.1.1 -n 1 -w 5000 > nul")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to restart PUBG: {str(e)}")
            
        
    """ def clear_cache(self):
        try:
            # Replace 'path_to_cache_folder' with the actual path to PUBG cache folder
            cache_folder_path = "path_to_cache_folder"
            for file_name in os.listdir(cache_folder_path):
                file_path = os.path.join(cache_folder_path, file_name)
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            messagebox.showinfo("Success", "Cache cleared successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clear cache: {str(e)}") """
            
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

        
def main():
    root = tk.Tk()
    root.geometry('300x200')
    app = PUBGLauncher(root)
    sv_ttk.set_theme("dark")
    root.mainloop()

if __name__ == "__main__":
    main()