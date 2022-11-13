import ctypes
import json

#Called when an error occurs, input: "code - error code, message - error message"
def messageHandler(code, message):
    debug = False
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

    #Convert the incoming data to a string.
    inc_data = str(inc_data)

    #Convert the incoming data to a readable format.
    inc_data = inc_data.replace("'",'"') 

    #Convert the incoming data to JSON.
    global data
    data = json.loads(inc_data)

    #With file open, dumps the data into the file.
    with open("jsonDataFile.json", 'w') as outfile:
        json.dump(data, outfile, indent=4)
        print("JSON File Written.")

        #Call the main function.
        main()

#Recives the webhook data and sends it towards the right files.
def main():
        #If data is not empty, continue.
        if data:
            #If the data requires "mediaPlayer", call mediaControlHandler in '/executer/media_controller.py'.
            if data['mediaPlayer']:
                import executer.media_controller as media_controller
                #Sends the data to the media controller.
                media_controller.mediaControlHandler(data)

            messageHandler(200, '')
        #If data is empty, return error.
        else:
            print("No Webhook JSON Recived. - Blank Webhook")
            messageHandler(400, '')


