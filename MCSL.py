import json
import os
import subprocess
import argparse

def read_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

def launch_server(server_name, config_path):
    config = read_config(config_path)
    if server_name not in config[0]:
        print(f"Server '{server_name}' not found in config file.")
        return

    server_config_path = config[0][server_name]
    server_config = read_config(server_config_path)
    
    print(f"Launching {server_name} server...")
    print(f"Description: {server_config[0]['Description']}")
    print(f"Version: {server_config[0]['Version']}")
    print("Starting server...")
    subprocess.run(server_config[0]['LaunchCommand'], shell=True)

def main():
    parser = argparse.ArgumentParser(description="Minecraft Server Launcher")
    parser.add_argument("server_name", type=str, help="Name of the server to launch")
    args = parser.parse_args()

    config = read_config("config.json")
    launch_server(args.server_name, config)

if __name__ == "__main__":
    main()
