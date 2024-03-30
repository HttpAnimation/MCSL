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
    curl -o install.bash https://github.com/HttpAnimation/MCSL/raw/main/install.bash
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
The configuration feature is currently under development. Stay tuned for updates on how to tailor your server settings to your preferences.

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