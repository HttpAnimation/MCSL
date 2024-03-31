# MCSL: Minecraft Server Launcher

## Introduction
MCSL is a simple yet powerful Minecraft server launcher designed to streamline the process of setting up and managing your Minecraft server. Whether you're hosting your own server for personal use or for a community of players, MCSL aims to make the experience smooth and hassle-free.

## Features
- Cross-platform compatibility: MCSL aims to support various operating systems including Linux, macOS, and Windows (NT).
- Easy installation: Installing MCSL is a breeze. Just follow the simple instructions below to get started.
- Simplified configuration: Customize your server settings with ease once the configuration feature is implemented.
- Error code reference: Encounter an issue? Refer to the error code section for quick troubleshooting.

## Installation
To install MCSL, follow these steps:
1. Open a terminal.
2. Make a new dir.

    ```bash
    mkdir ~/MCSL
    ```
3. Enter the dir.

    ```bash
    cd ~/MCSL
    ```

4. Download the installer script.

    ```bash
    curl -O -L https://github.com/HttpAnimation/MCSL/raw/main/install.bash
    ```

5. Allow the script to execute commands.

    ```bash
    chmod +x install.bash
    ```

6. Run the installer.

    ```bash
    ./install.bash
    ```

7. Remove the installer.

    ```bash
    rm install.bash
    ```

## Configuration
The config file called **config.conf** open up the file with a text edit for this guide let's use nano.

```bash
$/ nano config.conf
```

Once in the file add the following to the file.

```bash
[Name]
LaunchCommand = 
Version = 
Description = 
```

Where it says name replace that with the name of your server **eg. MyServer**

```bash
[MyServer]
LaunchCommand = 
Version = 
Description = 
```

For the version enter the version of your minecraft server **eg. 1.12.2**

```bash
[MyServer]
LaunchCommand = 
Version = 1.12.2
Description = 
```

For the description you can put what ever you want **eg. My simple minecraft server**

```bash
[MyServer]
LaunchCommand = 
Version = 1.12.2
Description = My simple minecraft server
```

For the LaunchCommnd this is where the command to run your server will go if your server is in a subfolder add **FOLDER/####.jar** to the run command let's use the fabric jar for this


```bash
[MyServer]
LaunchCommand = fajava -Xmx2G -jar fabric-server-mc.1.20.4-loader.0.15.7-launcher.1.0.0.jar nogui
Version = 1.12.2
Description = My simple minecraft server
```

```bash
[MyServer]
LaunchCommand = java -Xmx2G -jar FOLDER/fabric-server-mc.1.20.4-loader.0.15.7-launcher.1.0.0.jar nogui
Version = 1.12.2
Description = My simple minecraft server
```

## Error Codes
Encountering an error? Here's what each error code means:

1. **Error code 1**:
    - Meaning: The server specified in your configuration file was not found.
    
2. **Error code 2**:
    - Meaning: No launch command was found for your server.
    
3. **Error code 3**:
    - Meaning: Your configuration file was not found.

Refer to these error codes to troubleshoot and resolve any issues you encounter.

## Credits
Special thanks to [FYC](https://github.com/HttpAnimation/FYC-Rewrite-V2/) for their JSON styling contributions to enhance the visual appeal of MCSL.

Special thanks to [Downloader](https://github.com/HttpAnimation/Downloader) for the downlaoder scripts.