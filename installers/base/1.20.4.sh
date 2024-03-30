#!/bin/bash

# Variables
minecraft_version="1.20.4"
download_url="https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar"
config="https://raw.githubusercontent.com/HttpAnimation/MCSL/main/installers/base/config.conf"
downloaded_file="baseServer${minecraft_version}.jar"
target_directory="Base${minecraft_version}"

# Download Minecraft server
echo "Downloading Minecraft ${minecraft_version}..."
curl -o "$downloaded_file" "$download_url"
echo "Downloading the config file ${minecraft_version}..."
curl -o "$config"
echo "Done downloading"

# Rename the downloaded server
echo "Renaming the downloaded server..."
mv "$downloaded_file" "${target_directory}.jar"
echo "Done renaming"

# Create a new directory
echo "Creating new directory..."
mkdir "$target_directory"
echo "Done creating directory"

# Move files to new directory
echo "Moving fils to new directory..."
mv "${target_directory}.jar" "$target_directory/baseServer${minecraft_version}.jar"
mv ""
echo "Done moving"

echo "Done :3"
