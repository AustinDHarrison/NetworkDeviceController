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

  var params = {
    "mediaControl": {
        "control": "playPause"
    }
}

  request.send(JSON.stringify(params));
}
function sendPostNext() {
  var request = new XMLHttpRequest();
  request.open("POST", "http://192.168.1.188:80/", true);

  request.setRequestHeader('Content-type', 'application/json');

  var params = {
    "mediaControl": {
        "control": "nextTrack"
    }
}

  request.send(JSON.stringify(params));
}