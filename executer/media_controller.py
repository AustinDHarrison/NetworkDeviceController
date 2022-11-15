import win32api
from win32con import KEYEVENTF_EXTENDEDKEY
import json
#Interprets the incoming data.
def mediaControlHandler():
    with open("jsonDataFile.json", "r") as jsonFileData:
        jsonData = json.load(jsonFileData)

        #Play/Pause
        if jsonData["mediaControl"]["playPauseToggle"] == True:
            togglePlayPause()
        if jsonData["mediaControl"]["nextTrack"]["value"] == True:

            if jsonData["mediaControl"]["nextTrack"]["repeat"] > 0:
                for x in range(jsonData["mediaControl"]["nextTrack"]["repeat"]):
                    nextTrack()
                    print("Next Track: ", x + 1)
            elif jsonData["mediaControl"]["nextTrack"]["repeat"] < 0:
                for x in range(jsonData["mediaControl"]["nextTrack"]["repeat"] * -1):
                    previousTrack()
                    print("Previous Track: ", x + 1)

def togglePlayPause():
    from win32con import VK_MEDIA_PLAY_PAUSE
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)

def nextTrack():
    from win32con import VK_MEDIA_NEXT_TRACK

    win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)

def previousTrack():
    from win32con import VK_MEDIA_PREV_TRACK

    win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)