const fs = require('fs-extra');

async function readConfig(configPath) {
    try {
        const data = await fs.readFile(configPath, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        console.error(`Error reading ${configPath}:`, error);
        return null;
    }
}

async function launchServer(serverConfig) {
    console.log(`Launching server: ${serverConfig.Description}`);
    console.log(`Version: ${serverConfig.Version}`);
    console.log(`Launch Command: ${serverConfig.LaunchCommand}`);

    // Execute the launch command
    // Add your code here to actually launch the server
}

async function main() {
    const config = await readConfig('config/config.json');

    if (!config) {
        console.error('Failed to read config file. Exiting...');
        return;
    }

    const serverName = Object.keys(config[0])[0];
    const serverConfigPath = config[0][serverName];

    const serverConfig = await readConfig(serverConfigPath);

    if (!serverConfig) {
        console.error('Failed to read server config file. Exiting...');
        return;
    }

    await launchServer(serverConfig[0]);
}

main();
