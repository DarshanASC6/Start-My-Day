import subprocess
import webbrowser
import json
import time
import playsound

with open('data.json') as f:
    data = json.load(f)
    # Import JSON compatability into the file


def open(filepath):
    subprocess.call(filepath)


def web(link):
    webbrowser.open(link)


time_count = 12


def timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    for i in range(0, 3):
        playsound.playsound('chime.mp3')
    print("take a break")


for i in data['open']['sites']:
    web(i['link'])
    # Opens up a Firefox browser window with a bunch of preset tabs

for item in data['open']['filepaths']:
    open(item['path'])
    # Opens up my IDE
