#!/bin/bash

echo "Downloading Minecraft 1.20.4..."
curl -o baseServer1.20.4.jar https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar
echo "Done downloading"

echo "Renaming the downloaded file..."
mv baseServer1.20.4.jar Base1.20.4.jar
echo "Done renaming"

echo "Making new directory..."
mkdir Base1.20.4
echo "Done making directory"

echo "Moving server to new directory..."
mv Base1.20.4.jar Base1.20.4/baseServer1.20.4.jar
echo "Done moving"

echo "Done :3"
