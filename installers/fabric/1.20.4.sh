#!/bin/bash

mkdir Downloading
cd Downloading

# Download Minecraft Jar file
wget -O fabric-server-mc.1.20.4-loader.0.15.7-launcher.1.0.0.jar https://github.com/HttpAnimation/MCSL/raw/main/installers/fabric/fabric-server-mc.1.20.4-loader.0.15.7-launcher.1.0.0.jar

# Download Config file
wget -O config.conf https://raw.githubusercontent.com/HttpAnimation/MCSL/main/installers/fabric/config.conf

# Set variables
MinecraftJarFile=fabric-server-mc.1.20.4-loader.0.15.7-launcher.1.0.0.jar
ConfFile=config.conf
NewFolder=Fabric-1.20.4

# Create directory
mkdir $NewFolder

# Move files
mv $MinecraftJarFile $NewFolder
mv $ConfFile $NewFolder

# Move folder
mv $NewFolder ..

# Return to initial directory
cd ..

# Remove temporary directory
rm -rf Downloading
