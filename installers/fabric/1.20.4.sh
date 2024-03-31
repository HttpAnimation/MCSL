mkdir Downloading
cd Downloading 

wget https://meta.fabricmc.net/v2/versions/loader/1.20.4/0.15.7/1.0.0/server/jar
wget https://raw.githubusercontent.com/HttpAnimation/MCSL/main/installers/fabric/config.conf

mkdir Fabric-1.20.4

mv fabric-server-mc.1.20.4-loader.0.15.7-launcher.1.0.0.jar Fabric-1.20.4
mv config.conf Fabric-1.20.4
mv Fabric-1.20.4 ../../
rm -rf Downloading