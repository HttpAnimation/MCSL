import json
import sys
import os

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def launch_server(server_name, config):
    if server_name not in config:
        print(f"Server '{server_name}' not found in config.")
        return

    server_data = config[server_name]
    launch_command = server_data.get('LaunchCommand')
    
    if not launch_command:
        print(f"No launch command found for server '{server_name}' in config.")
        return

    os.system(launch_command)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 MCSL.py <server_name>")
        return

    server_name = sys.argv[1]
    config_file = 'config.json'

    if not os.path.exists(config_file):
        print("Config file 'config.json' not found.")
        return

    config = load_config(config_file)
    launch_server(server_name, config)

if __name__ == "__main__":
    main()
