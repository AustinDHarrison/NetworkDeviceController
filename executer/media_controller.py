import win32api
from win32con import KEYEVENTF_EXTENDEDKEY
import json
import math

#Interprets the incoming data.
def mediaControlHandler():
    with open("jsonDataFile.json", "r") as jsonFileData:
        jsonData = json.load(jsonFileData)

        #Play/Pause
        if jsonData["mediaControl"]["playPauseToggle"] == True:
            togglePlayPause()

        #Track - Next
        if jsonData["mediaControl"]["nextTrack"]["value"] == True:
            nextTrack()
            if jsonData["mediaControl"]["nextTrack"]["repeat"] > 0:
                for x in range(jsonData["mediaControl"]["nextTrack"]["repeat"]):
                    nextTrack()
                    print("Next Track: ", x + 1)
        #Track - Previous
            elif jsonData["mediaControl"]["nextTrack"]["repeat"] < 0:
                if jsonData["mediaControl"]["nextTrack"]["repeat"] == -1:
                    previousTrack()
                    previousTrack()
                    print("Previous Track: 1")
            else:
                for x in range(jsonData["mediaControl"]["nextTrack"]["repeat"] * -1):
                    previousTrack()#
                    print("Previous Track: ", x + 1)
        #Volume
        if jsonData["mediaControl"]["volume"]["increment"] != 0:
            volumeSet(jsonData["mediaControl"]["volume"]["increment"])

def togglePlayPause():
    print("Play/Pause")
    from win32con import VK_MEDIA_PLAY_PAUSE
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)

def nextTrack():
    from win32con import VK_MEDIA_NEXT_TRACK
    win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)

def previousTrack():
    from win32con import VK_MEDIA_PREV_TRACK

    win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)


#Volume is a value between -100 and 100.
def volumeSet(incriment):
    #Tests if the incriment is a valid value.
    empty = bool(incriment)
    #If the incriment is not a valid value, the function will display an error.
    if empty == False:
        import executer.error_handler as error_handler
        error_handler.errorHandler("custom", "Volume incriment is empty. Please submit a value with your request.")

    #If the increment is over 100, the function will display an error.
    elif incriment > 100:
        import executer.error_handler as error_handler
        error_handler.errorHandler("custom", "Volume incriment is too high. Max is 100.")
    #If the increment is under -100, the function will display an error.
    elif incriment < -100:
        import executer.error_handler as error_handler
        error_handler.errorHandler("custom", "Volume incriment is too low. Minimum is -100.")

    #If the incriment is a valid value, the function will continue.
    elif incriment > 0:
        #Positive Incriment
        from win32con import VK_VOLUME_DOWN
        from win32con import VK_VOLUME_UP

        #The volume is set to 0 so the volume can be set precisely.
        a= 0
        while a < 100:
            print("Volume Reset: ", a)
            win32api.keybd_event(VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)
            a += 1
        
        #The volume is set to the desired value.
        y = 0
        #Due to windows volume only being able to be set in increments of 2, the incriment is divided by 2, So users can be more precise in their requests.
        incriment /= 2

        while y < incriment:
            print("Volume Up: ", y + 1)
            win32api.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)
            y += 1
    #If the request is a negative value, the function will continue.
    else:
        #Negative Incriment
        from win32con import VK_VOLUME_DOWN
        y = 0
        #Due to windows volume only being able to be set in increments of 2, the incriment is divided by 2, So users can be more precise in their requests.
        incriment /= 2
        while y > incriment:
            print("Volume Down: ", y)
            win32api.keybd_event(VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)
            y -= 1