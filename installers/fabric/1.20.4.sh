#!/bin/bash

mkdir downloading
cd downloading

# Variables
minecraft_version="1.20.4"
download_url="https://meta.fabricmc.net/v2/versions/loader/1.20.4/0.15.7/1.0.0/server.jar"
config_url="https://raw.githubusercontent.com/HttpAnimation/MCSL/main/installers/fabric/1.20.4/config.conf"
downloaded_file="baseServer${minecraft_version}.jar"
config_file="config.conf"
target_directory="Fabric"  # Updated directory name

# Download Minecraft server
echo "Downloading Minecraft ${minecraft_version}..."
curl -OJ "$downloaded_file" "$download_url"
echo "Done downloading"

# Rename the downloaded server
echo "Renaming the downloaded server..."
mv "$downloaded_file" "${target_directory}/baseServer${minecraft_version}.jar"
echo "Done renaming"

# Create a new directory
echo "Creating new directory..."
mkdir "$target_directory"
echo "Done creating directory"

# Download and move config file to new directory
echo "Downloading and moving the config file..."
curl -o "$config_file" "$config_url"
mv "$config_file" "$target_directory/$config_file"
echo "Done moving"

echo "Done :3"
echo "Make sure to edit your config.conf file with your new one."


# Fabric
mv Fabric ../Fabric-1.20.4