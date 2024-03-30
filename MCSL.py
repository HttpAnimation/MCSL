import json
import subprocess
import os
import sys

class MinecraftServerLauncher:
    def __init__(self, config_file):
        self.config_file = config_file
        self.servers = {}

    def load_config(self):
        with open(self.config_file, 'r') as f:
            config_data = json.load(f)
            for server_name, server_config_path in config_data.items():
                with open(server_config_path, 'r') as server_config_file:
                    server_config = json.load(server_config_file)
                    self.servers[server_name] = server_config

    def list_servers(self):
        print("Available Servers:")
        for server_name in self.servers.keys():
            print(f"- {server_name}")

    def launch_server(self, server_name):
        if server_name not in self.servers:
            print(f"Server '{server_name}' not found in the configuration.")
            return
        
        server_config = self.servers[server_name]
        launch_command = server_config.get('LaunchCommand')
        if not launch_command:
            print(f"No launch command specified for server '{server_name}'.")
            return

        print(f"Launching server '{server_name}'...")
        subprocess.call(launch_command, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python MCSL.py <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]

    if not os.path.isfile(config_file):
        print(f"Config file '{config_file}' not found.")
        sys.exit(1)

    mcsl = MinecraftServerLauncher(config_file)
    mcsl.load_config()

    while True:
        mcsl.list_servers()
        server_name = input("Enter the name of the server to launch (or 'exit' to quit): ").strip()
        
        if server_name.lower() == 'exit':
            break
        
        mcsl.launch_server(server_name)
