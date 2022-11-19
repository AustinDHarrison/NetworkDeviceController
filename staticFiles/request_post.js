function sendPostWithData() {
  var data = document.getElementById('dataInput').value;

  var request = new XMLHttpRequest();
  request.open("POST", "http://192.168.1.188:80/", true);

  request.setRequestHeader('Content-type', 'application/json');

  var params = JSON.parse(data);
  console.log(params);
  request.send(JSON.stringify(params));
}
function sendPost() {
  var request = new XMLHttpRequest();
  request.open("POST", "http://192.168.1.188:80/", true);

  request.setRequestHeader('Content-type', 'application/json');

  var params =     { "braviaTVControl" : {
    "config": {    
        "ip" : "192.168.1.129",
        "pin" : "2338",
        "nickname" : "DeviceName",
        "deviceID" : "1234567890"
    },
    "event" : {
      "value": "start_app",
      "args": "Freevee"
    }
    }
} 

  request.send(JSON.stringify(params));
}
function sendPostNext() {
  var request = new XMLHttpRequest();
  request.open("POST", "http://192.168.1.188:80/", true);

  request.setRequestHeader('Content-type', 'application/json');

  var params =     {
    "mediaControl": {
        "playPauseToggle": false,
        "nextTrack": {
            "value": true,
            "repeat": 1
        },
        "volume": {
            "increment": 0,
            "repeat": 0
        }
    }
}

  request.send(JSON.stringify(params));
}