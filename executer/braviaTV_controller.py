import json
from bravia_tv import BraviaRC
import executer.error_handler as error_handler
def braviaTVControlHandler():
    with open("jsonDataFile.json", "r") as jsonFileData:
        jsonData = json.load(jsonFileData)


        #Config - Get ip address from the json file.
        if jsonData["braviaTVControl"]["config"]["ip"]:
            
            if jsonData["braviaTVControl"]["config"]["ip"] == "":
                ip_address = "192.168.1.129"
            else:
                ip_address = jsonData["braviaTVControl"]["config"]["ip"]

        #Config - Get pin from the json file.
        if jsonData["braviaTVControl"]["config"]["pin"] == "0000" or "":
            pin = "0000"
        else:
            pin = jsonData["braviaTVControl"]["config"]["pin"]

        #Config - Get the nickname from the json file.
        if jsonData["braviaTVControl"]["config"]["nickname"]:
            nickname = jsonData["braviaTVControl"]["config"]["nickname"]

        #Config - Get the deviceID from the json file.
        if jsonData["braviaTVControl"]["config"]["deviceID"]:
            deviceID = jsonData["braviaTVControl"]["config"]["deviceID"]

        if jsonData["braviaTVControl"]["event"]["args"]:
            eventArgs = jsonData["braviaTVControl"]["event"]["args"]
        else:
            eventArgs = ""

        if jsonData["braviaTVControl"]["event"]["value"]:
            event = jsonData["braviaTVControl"]["event"]["value"]
        if jsonData["braviaTVControl"]["event"]["value"] == "init":
            connect_init(ip_address, pin, nickname, deviceID)
        else:
            connect_with_event(ip_address, pin, nickname, deviceID, event, eventArgs)
            
        
        #Init won't call an event, it will only connect to the tv for pin configuration.
    #Calls the send function.

#Called if event is "init", used for pin configuration.
def connect_init(ip_address, pin, nickname, deviceID):
    #Connect to the tv.
    braviarc = BraviaRC(ip_address)
    braviarc.connect(pin, deviceID, nickname)
    print("Updated pin with the pin displayed on your TV screen. If you don't see a pin, your deviceID is already affiliated with a pin. Remember the pin, or delete the device from your TV.")

def connect_with_event(ip_address, pin, nickname, deviceID, event, eventArgs):
    #Connect to the tv.
    braviarc = BraviaRC(ip_address)
    braviarc.connect(pin, deviceID, nickname)
    #Sends the event to the tv.
    if eventArgs:
        if event == "start_app":
            eventArgs = "\"" + eventArgs + "\""
            print(eventArgs)
            a = braviarc.start_app("Amazon Prime")
            print(a)
        else:
            send_event = getattr(braviarc, event)
            send_event(eventArgs)
    else:
        send_event = getattr(braviarc, event)
        send_event()