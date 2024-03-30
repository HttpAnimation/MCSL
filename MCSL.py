import sys
import json
import subprocess

def load_config(config_file):
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Config file '{config_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in config file '{config_file}'.")
        sys.exit(1)

def launch_server(server_name, config):
    if server_name in config:
        server_config_path = config[server_name]
        server_config = load_config(server_config_path)
        launch_command = server_config.get('LaunchCommand')
        if launch_command:
            print(f"Launching {server_name}...")
            subprocess.run(launch_command, shell=True)
        else:
            print(f"Error: Launch command not found for server '{server_name}' in config file '{server_config_path}'.")
    else:
        print(f"Error: Server '{server_name}' not found in config file.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 MCSL.py <ServerName>")
        sys.exit(1)

    config_file = 'config.json'
    server_name = sys.argv[1]

    config = load_config(config_file)
    if isinstance(config, list):
        # If the config is a list, assume it contains dictionaries and use the first element
        config = config[0]

    launch_server(server_name, config)

if __name__ == "__main__":
    main()
