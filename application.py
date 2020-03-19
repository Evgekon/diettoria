from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    current_ver = get_version()
    return render_template('main.html', current_ver=current_ver)


@app.route('/version', methods=['POST', 'GET'])
def version(ver=None):
    if request.method == 'POST':
        ver = request['ver']
        set_version(ver)
    else:
        return str(get_version())

def get_version():
    with open("ver.json", "r+") as read_file:
        data = json.load(read_file)
        return data['ver']

def set_version(ver):
    data = {'ver': ver}
    with open("ver.json", "w") as write_file:
        json.dump(data, write_file)
    return

app.run()
