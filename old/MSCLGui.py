import configparser
import sys
import os
import tkinter as tk
from tkinter import messagebox

ERROR_SERVER_NOT_FOUND = 1
ERROR_NO_LAUNCH_COMMAND = 2
ERROR_CONFIG_NOT_FOUND = 3

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def launch_server():
    server_name = entry_server_name.get()
    if not server_name:
        messagebox.showerror("Error", "Please enter a server name.")
        return

    if not config.has_section(server_name):
        messagebox.showerror("Error", f"Server '{server_name}' not found in config.")
        return

    launch_command = config.get(server_name, 'LaunchCommand')
    version = config.get(server_name, 'Version')
    description = config.get(server_name, 'Description')
    
    if not launch_command:
        messagebox.showerror("Error", f"No launch command found for server '{server_name}' in config.")
        return

    messagebox.showinfo("Launching Server", f"Launching {server_name} ({description}) - Version {version}")
    os.system(launch_command)

def main():
    if not os.path.exists('config.conf'):
        messagebox.showerror("Error", "Config file 'config.conf' not found.")
        return

    global config
    config = load_config('config.conf')

    root = tk.Tk()
    root.title("MCSL Launcher")

    label_server_name = tk.Label(root, text="Enter Server Name:")
    label_server_name.pack()

    global entry_server_name
    entry_server_name = tk.Entry(root)
    entry_server_name.pack()

    btn_launch_server = tk.Button(root, text="Launch Server", command=launch_server)
    btn_launch_server.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
