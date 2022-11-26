function playPauseToggle() {
  var request = new XMLHttpRequest();
  request.open("POST", "http://192.168.1.188:80/", true);

  request.setRequestHeader('Content-type', 'application/json');

  var params = {
    "mediaControl": {
        "playPauseToggle": true,
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

  request.send(JSON.stringify(params));
}
function changeTrack(repeat) {
  var request = new XMLHttpRequest();
  request.open("POST", "http://192.168.1.188:80/", true);

  request.setRequestHeader('Content-type', 'application/json');

  var params =     {
    "mediaControl": {
        "playPauseToggle": false,
        "nextTrack": {
            "value": true,
            "repeat": repeat
        },
        "volume": {
            "increment": 0,
            "repeat": 0
        }
    }
}
  console.log(params);
  request.send(JSON.stringify(params));
}
function changeVolume() {
  var request = new XMLHttpRequest();
  request.open("POST", "http://192.168.1.188:80/", true);
  var data = parseInt(document.getElementById("volumeInput").value);
  request.setRequestHeader('Content-type', 'application/json');
  var params = {
    "mediaControl": {
        "playPauseToggle": false,
        "nextTrack": {
            "value": false,
            "repeat": 1
        },
        "volume": {
            "increment": data,
            "repeat": 0
        }
    }
}
console.log(params);
  request.send(JSON.stringify(params));
}


function changeVolume() {
  var request = new XMLHttpRequest();
  request.open("POST", "http://192.168.1.188:80/", true);
  var data = parseInt(document.getElementById("volumeInput").value);
  request.setRequestHeader('Content-type', 'application/json');
  const params = {
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
console.log(params);
  request.send(JSON.stringify(params));
}


