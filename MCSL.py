import json
import os
import subprocess
import argparse

def read_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

def launch_server(server_name, config_path):
    config = read_config(config_path)
    print(f"Launching {server_name} server...")
    print(f"Description: {config[0]['Description']}")
    print(f"Version: {config[0]['Version']}")
    print("Starting server...")
    subprocess.run(config[0]['LaunchCommand'], shell=True)

def print_server_names():
    config = read_config("config.json")
    print("Available servers:")
    for server_name in config[0]:
        if server_name != "ServerNameHere":
            print(server_name)

def main():
    parser = argparse.ArgumentParser(description="Minecraft Server Launcher")
    parser.add_argument("server_name", nargs='?', type=str, help="Name of the server to launch")
    args = parser.parse_args()

    if args.server_name is None:
        print_server_names()
        return

    config = read_config("config.json")
    if args.server_name not in config[0]:
        print("Server not found in config file.")
        return

    launch_server(args.server_name, config[0][args.server_name])

if __name__ == "__main__":
    main()
