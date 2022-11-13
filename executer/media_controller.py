import win32api
from win32con import KEYEVENTF_EXTENDEDKEY

def mediaControlHandler(data):
    if data['mediaPlayer']['control'] == 'playPause':
        togglePlayPause()
    elif data['mediaPlayer']['control'] == 'nextTrack':
        nextTrack()
    else:
        print("No media player action found.")



def togglePlayPause():

    from win32con import VK_MEDIA_PLAY_PAUSE

    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
    # https://learn.microsoft.com/uk-ua/windows/win32/inputdev/virtual-key-codes

def nextTrack():
    from win32con import VK_MEDIA_NEXT_TRACK

    win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)