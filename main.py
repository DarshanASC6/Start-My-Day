import subprocess
import time
import playsound
import webbrowser
import json


t = 1200
# 20 minutes but written in seconds

# Import JSON compatability into the file
with open('data.json') as f:
    data = json.load(f)


def timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    for i in range(0, 5):
        playsound.playsound('chime.mp3')


def open(filepath):
    subprocess.call(filepath)


for filepaths in data['open']['filepaths']:
    open(filepaths['path'])
# Opens up my IDE and a Firefox browser window

# for i in data['open']['sites']:
#     print(i['link'])
# # Should print all of the links I have in my JSON file

# webbrowser.open('http://www.python.org')
# for i in range(0, 3):
#     timer(t)
