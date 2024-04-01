import subprocess
import webbrowser
import threading
from flask import Flask, render_template, request, jsonify
import tkinter as tk

# Flask app
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

def start_flask_app():
    app.run()

# Tkinter app
def open_browser():
    webbrowser.open('http://127.0.0.1:5000')

def start_flask_thread():
    flask_thread = threading.Thread(target=start_flask_app)
    flask_thread.daemon = True
    flask_thread.start()

def start_flask_and_browser():
    start_flask_thread()
    root.after(1000, open_browser)

root = tk.Tk()
root.title("MCSL - HttpAnimation")

# Start Flask and open browser
start_flask_and_browser()

root.mainloop()
