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