import configparser
import sys
import os
import socket

ERROR_SERVER_NOT_FOUND = 1
ERROR_NO_LAUNCH_COMMAND = 2
ERROR_CONFIG_NOT_FOUND = 3

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def launch_server(server_name, config):
    if not config.has_section(server_name):
        print(f"Error ({ERROR_SERVER_NOT_FOUND}): Server '{server_name}' not found in config.")
        return

    launch_command = config.get(server_name, 'LaunchCommand')
    version = config.get(server_name, 'Version')
    description = config.get(server_name, 'Description')
    
    if not launch_command:
        print(f"Error ({ERROR_NO_LAUNCH_COMMAND}): No launch command found for server '{server_name}' in config.")
        return

    print(f"Launching {server_name} ({description}) - Version {version}")

    # Retrieve IP address of the PC
    ip_address = socket.gethostbyname(socket.gethostname())

    # Modify launch command to use IP address
    modified_launch_command = launch_command.replace("{ip_address}", ip_address)

    os.system(modified_launch_command)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 MCSL.py <server_name>")
        return

    server_name = sys.argv[1]
    config_file = 'config.conf'

    if not os.path.exists(config_file):
        print(f"Error ({ERROR_CONFIG_NOT_FOUND}): Config file 'config.conf' not found.")
        return

    config = load_config(config_file)
    launch_server(server_name, config)

if __name__ == "__main__":
    main()
