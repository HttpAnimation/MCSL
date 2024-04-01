import configparser
import subprocess
import os

# Read config file
config = configparser.ConfigParser()
config.read('config.conf')

# Display server information
for server in config.sections():
    print(f"{server} V:{config[server]['MinecraftVersion']} | Modded = {config[server]['Modded']} | Description: {config[server]['Description']}")

# Prompt user for server selection
selected_server = input("Enter the name of the server to launch: ")

# Check if selected server exists in config
if selected_server not in config.sections():
    print("Invalid server name.")
    exit()

# Get launch command for selected server
launch_command = config[selected_server]['LaunchCommand']

# Extract directory from launch command
server_directory = os.path.dirname(launch_command.split(' ')[-2])

# Change directory if specified
if server_directory:
    os.chdir(server_directory)

# Execute launch command
subprocess.run(launch_command, shell=True)
