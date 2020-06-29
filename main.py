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


def web(link):
    webbrowser.open_new(link)


for filepaths in data['open']['filepaths']:
    open(filepaths['path'])
    # Opens up my IDE

for i in data['open']['sites']:
    web(i['link'])
    # Opens up a Firefox browser window with a bunch of preset tabs


# for i in range(0, 3):
#     timer(t)
