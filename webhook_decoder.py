import json
import executer.error_handler as error_handler

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
            if jsonData['debug']['action'] == "selfDestruct":
                print ("Self Destruct Recived")
                from app import selfDestruct
                selfDestruct()
            #Calls the message handler.
            error_handler.messageHandler(686, 'Debug toggled.')
            print("Debug toggled.")
            
        if jsonData.get('browserControl',0):
            import executer.browser_controller as browser_controller
            #Calls the web control handler.
            browser_controller.webControlHandler()
        #If the data requires "mediaControl", call mediaControlHandler in '/executer/media_controller.py'.
        if jsonData.get('mediaControl', 0):
            import executer.media_controller as media_controller
            media_controller.mediaControlHandler()
        #If the data requires "braviaTVControl", call braviaTVControlHandler in '/executer/braviaTV_controller.py'.
        if jsonData.get('braviaTVControl', 0):
            import executer.braviaTV_controller as braviaTV_controller
            braviaTV_controller.braviaTVControlHandler()