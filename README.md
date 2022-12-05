# NetworkDeviceController - [192.168.1.???](http://192.168.1.188/)
### **Required Pips**
    pip install sys
    pip install flask


## **_Executers_**
#
##  **Media Controller**
### **Required Pips**
    pip install --upgrade pywin32


### **JSON Template**

    {
        "mediaControl": {
            "playPauseToggle": false,
            "track": {
                "next": false,
                "previous": false,
                "repeat": 0
            },
            "volume": {
                "increment": 0,
                "repeat": 0
            }
        }
    }
* [Microsoft Virtual Key Codes Cheat Sheet.](https://learn.microsoft.com/en-gb/windows/win32/inputdev/virtual-key-codes)
### **"playPauseToggle"**
* Takes a boolean input, for example: **Incorrect -** *{"playPauseToggle": "false"}*, **Correct -** *{"playPauseToggle": false}*.
### **"track"**
* Takes a boolean input, for example: **Incorrect -** *{"nextTrack": {"value": "false"}*, **Correct -** *{"nextTrack": {"value": false}*.
### **"volume"**
* Takes an intager input.
* If the increment inputed is **odd**, it will be **rounded up to the next even number**. This is because windows volume controls only lets it go up in increments of two.
* The increment range is **100 to -100**. If you go out of this range an  **sever side error** *(not client side, the user will not recive an error)* will be thrown, check your values or limit how a user inputs the value.
#

## **Web Controller**
### **Required Pips**
    pip install webbrowser

#

## **Bravia TV Controller**
### **Required Pips**
    pip install bravia_tv
### **JSON Template**
    {
        "braviaTVControl": {
            "config": {
                "ip": "192.168.1.129",
                "pin": "2338",
                "nickname": "DeviceName",
                "deviceID": "1234567890"
            },
            "event": {
                "value": "event",
                "args": "eventArgs"
            }
        }
    }

* ***"IP"*** - The IP address of the TV, if left blank the script will conntect to 192.168.1.129.
* ***"PIN"*** - The pin used to identify your device the TV, by making the pin balnk or 0000 the tv will display a pin on the screen.
* ***"NICKNAME"*** - The name of the server, this will be used by the tv to identify the server.
* ***"DEVICEID"*** - The ID that the TV will use to identify the server, if left blank will be set to 0000.
### **Events**

* **Power**
    * turn_on
    * turn_off
    * get_power_status
