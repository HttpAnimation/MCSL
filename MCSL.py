import subprocess
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
    launch_command = request.form['server']
    if launch_command:
        process = subprocess.Popen(launch_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        output = stdout.decode() + '\n' + stderr.decode()
        return jsonify({'output': output})
    else:
        return jsonify({'error': 'No launch command specified.'})

if __name__ == '__main__':
    app.run(debug=True)
