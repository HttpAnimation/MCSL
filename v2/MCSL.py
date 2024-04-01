import subprocess
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def read_config_file(filename):
    config = {}
    with open(filename, 'r') as file:
        server_data = {}
        for line in file:
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                server_name = line[1:-1]
                config[server_name] = server_data
                server_data = {}
            elif '=' in line:
                key, value = line.split('=', 1)
                server_data[key.strip()] = value.strip()
    return config

@app.route('/')
def index():
    config = read_config_file('config.conf')
    return render_template('index.html', servers=config)

@app.route('/launch', methods=['POST'])
def launch_server():
    config = read_config_file('config.conf')
    server_name = request.form.get('server')
    launch_command = config.get(server_name, {}).get('LaunchCommand')
    if launch_command:
        os.system(launch_command)
        return jsonify({'output': 'Server launched successfully.'})
    else:
        return jsonify({'error': 'No launch command specified for the selected server.'})

if __name__ == '__main__':
    app.run(debug=True)
