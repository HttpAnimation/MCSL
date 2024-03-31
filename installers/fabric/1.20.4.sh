mkdir Downloading
cd Downloading 

MinecraftJarFile = https://meta.fabricmc.net/v2/versions/loader/1.20.4/0.15.7/1.0.0/server/jar
ConfFile = https://raw.githubusercontent.com/HttpAnimation/MCSL/main/installers/fabric/config.conf
NewFolder = Fabric-1.20.4

mkdir $NewFolder

mv fabric-server-mc.1.20.4-loader.0.15.7-launcher.1.0.0.jar $NewFolder
mv $ConfFile $NewFolder
mv $NewFolder ../../
rm -rf Downloading