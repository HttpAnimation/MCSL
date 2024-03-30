echo "Download minecraft 1.20.4."
curl -o https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar
echo "Done downloading"
echo "Ranaming the downloaded file"
mv server.jar baseServer1.20.4.jar
echo "Done renaming"
echo "Making new dir"
mkdir Base1.20.4
echp "Done making dir"
echo "Moving server to new dir"
cp baseServer1.20.4.jar Base1.20.4/baseServer1.20.4.jar
echo "Down moving"
echo "Done :3"