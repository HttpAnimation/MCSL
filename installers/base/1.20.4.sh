#!/bin/bash

# Variables
minecraft_version="1.20.4"
download_url="https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar"
config_url="https://raw.githubusercontent.com/HttpAnimation/MCSL/main/installers/base/config.conf"
downloaded_file="baseServer${minecraft_version}.jar"
config_file="config.conf"
target_directory="Base${minecraft_version}"

# Download Minecraft server
echo "Downloading Minecraft ${minecraft_version}..."
curl -o "$downloaded_file" "$download_url"
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
