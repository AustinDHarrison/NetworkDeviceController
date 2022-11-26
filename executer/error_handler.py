def errorHandler(code, message):
    debug = True
    if debug == True:
        import ctypes
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
        elif code == 683:
            print("Event Error. - 683")
            ctypes.windll.user32.MessageBoxW(0, message, "683", 0)
        elif code == "custom":
            print("Error.")
            ctypes.windll.user32.MessageBoxW(0, message, "Error.", 0)
        else:
            print("Event recived. - 506")
            ctypes.windll.user32.MessageBoxW(0, message, "506", 0)
    if debug == False:
        if code == 200:
            print("Webhook Recived. - 200")
        elif code == 400:
            if message == '':
                print("No Webhook Recived. - Blank Webhook")
            else:
                print("Improper webhook request. - 400")
        elif code == 401:
            print("Invalid webhook secret. - 401")
        elif code == 404:
            print("Webhook not found. - 404") 
        elif code == 500:
            print("Internal server error. - 500")
        elif code == 0:
            print("Unknown Error. - 0")
        elif code == 686:
            print("Debug toggled. - 686")
        elif code == 683:
            print("Event Error. - 683", message)
        elif code == "custom":
            print("Error.", message)
        else:
            print("Event recived. - 506 - ", message)
 
  

