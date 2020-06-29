import subprocess
import webbrowser
import json

with open('data.json') as f:
    data = json.load(f)
    # Import JSON compatability into the file


def open(filepath):
    subprocess.call(filepath)


def web(link):
    webbrowser.open(link)


for i in data['open']['sites']:
    web(i['link'])
    # Opens up a Firefox browser window with a bunch of preset tabs


for filepaths in data['open']['filepaths']:
    open(filepaths['path'])
    # Opens up my IDE
