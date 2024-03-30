import configparser
import sys
import os

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def launch_server(server_name, config):
    if not config.has_section(server_name):
        print(f"Server '{server_name}' not found in config.")
        return

    launch_command = config.get(server_name, 'LaunchCommand')
    version = config.get(server_name, 'Version')
    description = config.get(server_name, 'Description')
    
    if not launch_command:
        print(f"No launch command found for server '{server_name}' in config.")
        return

    print(f"Launching {server_name} ({description}) - Version {version}")
    os.system(launch_command)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 MCSL.py <server_name>")
        print("Usage: python MCSL.py <server_name>")
        return

    server_name = sys.argv[1]
    config_file = 'config.conf'

    if not os.path.exists(config_file):
        print("Config file 'config.conf' not found.")
        return

    config = load_config(config_file)
    launch_server(server_name, config)

if __name__ == "__main__":
    main()
