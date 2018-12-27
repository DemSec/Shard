from flask import Flask, request, render_template#, send_file
app = Flask(__name__)

import control as Control
import drivers as Drive
import subprocess as Subprocess

# Update Shard
Subprocess.run("cd /var/www/Shard && sudo git pull")

Drive.setup()

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def control():
	return Control.run(request)

@app.route('/test', methods=['GET'])
def test():
	return render_template('test.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
