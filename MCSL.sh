#!/bin/bash

# Function to read JSON file and extract value by key
read_json_value() {
    local json=$1
    local key=$2
    echo $(jq -r ".$key" <<< "$json")
}

# Function to launch Minecraft server
launch_server() {
    local launch_command=$1
    echo "Launching Minecraft server..."
    eval "$launch_command"
}

# Main function
main() {
    # Check if config file exists
    if [ ! -f "config.json" ]; then
        echo "Error: config.json not found!"
        exit 1
    fi

    # Read config.json
    config_json=$(cat config.json)

    # Check if config file is empty
    if [ -z "$config_json" ]; then
        echo "Error: config.json is empty!"
        exit 1
    fi

    # Get server names and their config file paths
    server_entries=$(jq -c '.[] | to_entries[]' <<< "$config_json")

    # Iterate through each server entry
    while IFS= read -r entry; do
        server_name=$(read_json_value "$entry" "key")
        config_path=$(read_json_value "$entry" "value")

        # Check if server config file exists
        if [ ! -f "$config_path" ]; then
            echo "Error: Server config file '$config_path' not found for server '$server_name'!"
            continue
        fi

        # Read server config file
        server_config=$(cat "$config_path")

        # Extract server details
        description=$(read_json_value "$server_config" "Description")
        launch_command=$(read_json_value "$server_config" "LaunchCommand")
        version=$(read_json_value "$server_config" "Version")

        # Print server information
        echo "Server: $server_name"
        echo "Description: $description"
        echo "Version: $version"

        # Ask user if they want to launch the server
        read -p "Do you want to launch this server? (y/n): " launch_input
        if [ "$launch_input" == "y" ]; then
            launch_server "$launch_command"
        fi

    done <<< "$server_entries"
}

# Call main function
main
