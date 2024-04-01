import subprocess
from flask import Flask, render_template_string, request

app = Flask(__name__)

def read_config_file(filename):
    config = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if '=' in line:
                key, value = line.strip().split('=')
                config[key.strip()] = value.strip()
    return config

@app.route('/')
def index():
    config = read_config_file('config.conf')
    server_name = list(config.keys())[0]
    return render_template_string('index.html', server_name=server_name, config=config)

@app.route('/launch', methods=['POST'])
def launch_server():
    launch_command = request.form['launch_command']
    process = subprocess.Popen(launch_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout.decode() + '\n' + stderr.decode()
    return output

if __name__ == '__main__':
    app.run(debug=True)
