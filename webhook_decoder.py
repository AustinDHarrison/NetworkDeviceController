import ctypes
import json

#Called when an error occurs, input: "code - error code, message - error message"
def messageHandler(code, message):
    debug = True
    if debug == True:
        if code == 200:
            print("Webhook Recived. - 200")
            ctypes.windll.user32.MessageBoxW(0, "Webhook Recived. ", "200", 0)
        elif code == 400:
            if message == '':
                print("No Webhook Recived. - Blank Webhook")
                ctypes.windll.user32.MessageBoxW(0, message, "No Webhook Recived. - Blank Webhook - 400", 0)
            else:
                print("Improper webhook request. - 400")
                ctypes.windll.user32.MessageBoxW(0, "Improper webhook request. ", "400", 0)
        elif code == 401:
            print("Invalid webhook secret. - 401")
            ctypes.windll.user32.MessageBoxW(0, "Invalid webhook secret. ", "401", 0)
        elif code == 404:
            print("Webhook not found. - 404")
            ctypes.windll.user32.MessageBoxW(0, "Webhook not found. ", "404", 0)
        elif code == 500:
            print("Internal server error. - 500")
            ctypes.windll.user32.MessageBoxW(0, "Internal server error. ", "500", 0)
        elif code == 0:
            print("Unknown Error. - 0")
            ctypes.windll.user32.MessageBoxW(0, "Unknown Error. ", "0", 0)
        elif code == 686:
            print("Debug toggled. - 686")
            ctypes.windll.user32.MessageBoxW(0, "Debug toggled. ", "686", 0)
        else:
            print("Event recived. - 506")
            ctypes.windll.user32.MessageBoxW(0, message, "506", 0)    

#Format the incoming data, packages it into a global variable and writes it to a file.
def formatIncData(inc_data):
    with open("jsonDataFile.json", "w") as write_file:
        json.dump(inc_data, write_file, indent=4)
    #Calls the main function.
    main()


#Recives the webhook data and sends it towards the right files.
def main():
    with open("jsonDataFile.json", "r") as jsonFileData:
        jsonData = json.load(jsonFileData)
        if jsonData.get('debug',0):
            #Calls the message handler.
            messageHandler(686, 'Debug toggled.')
            print("Debug toggled.")
        if jsonData.get('browserControl',0):
            import executer.browser_controller as browser_controller
            #Calls the web control handler.
            browser_controller.webControlHandler()
        #If the data requires "mediaControl", call mediaControlHandler in '/executer/media_controller.py'.
        if jsonData.get('mediaControl', 0):
            import executer.media_controller as media_controller
            media_controller.mediaControlHandler()