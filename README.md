# WebhookReciver

## **Local Python Server**
### **Required Pips**
    pip install flask


## **_Executers_**
#
##  **Media Controller**
### **Required Pips**
    pip install --upgrade pywin32'


### JSON Template

    {
        "mediaControl": {
            "playPauseToggle": false,
            "nextTrack": {
                "value": false,
                "repeat": 0
            },
            "volume": {
                "increment": 0,
                "repeat": 0
            }
        }
    }
* <https://learn.microsoft.com/uk-ua/windows/win32/inputdev/virtual-key-codes>

#

## **Web Controller**
### **Required Pips**
    pip install webbrowser

#

## **Bravia TV Controller**
### **Required Pips**
    pip install bravia_tv
### **JSON Template**
    { "braviaTVControl" : {
        "config": {    
            "ip" : "192.168.1.129",
            "pin" : "0000",
            "connectionDeviceName" : "DeviceName"
        },
        "event" : "powerOn"
        }
    } 

* ***"IP"*** - The IP address of the TV, if left blank the script will conntect to 192.168.1.129.
* ***"PIN"*** - The pin used to identify your device the TV, by making the pin balnk or 0000 the tv will display a pin on the screen.
* ***"connectionDeviceName"*** - The name of the server, this will be used by the tv to identify the server.

### **Events**
* **Power**
    * turn_on
    * turn_off
    * get_power_status