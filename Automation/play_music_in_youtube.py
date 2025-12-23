import time
import pywhatkit as kt
import random
from DLG import playsong, playing_dlg
from body.speak import speak


def play_music_on_youtube(text):
    playdlg = random.choice(playsong)
    speak(playdlg,3)
    kt.playonyt(text)
    time.sleep(3)
    playdlg =random.choice(playing_dlg)
    speak(playdlg+text,3)

