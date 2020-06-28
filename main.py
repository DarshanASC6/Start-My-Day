import subprocess
import datetime
import playsound



# Helpful
# https://www.youtube.com/watch?v=1iz4iwjUWTQ
# https://www.programiz.com/python-programming/datetime/current-time

Atom = 'C:\\Users\\ASCStudent\\AppData\\Local\\atom\\atom.exe'
Firefox = '"C:\\Program Files\\Mozilla Firefox\\firefox.exe"'

time = 1200

def timer(time):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        playsound.playsound('chime.mp3')


def open(filepath):
    subprocess.call(filepath)

open(Atom)
