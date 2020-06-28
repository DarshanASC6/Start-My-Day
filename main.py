import subprocess
import time
import playsound
# import webbrowser
import json


t = 1200

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


# for filepaths in data['open']:
#     print(filepaths)

# open(Atom)
# Opens my IDE
# for i in range(0,3):
#     open(Firefox)
#     webbrowser.open()
#     # Opens 3 Firefox browsers
# for i in range(0,3):
#     timer(t)
