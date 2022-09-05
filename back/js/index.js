var getJSON = function(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status === 200) {
        callback(null, xhr.response);
      } else {
        callback(status, xhr.response);
      }
    };
    xhr.send();
};

function callback(status, json){
    var table = document.getElementsByTagName("table")[0];
    var rows = table.getElementsByTagName("tr");
    var  i = 0;
    for(var key in json){
        if (key == "online"){
            i++;
            continue;
        }
        var cels = rows[i].getElementsByTagName("td");
        cels[0].innerHTML  = key;
        cels[1].innerHTML  = json[key];
        i+=1; 
    }
    var h2 = document.getElementById("online_stat");
    if (json["online"]) h2.innerHTML = "online";
    else h2.innerHTML = "offline";
}
function UpdateHtml(){
    getJSON("/get_data", callback);
}
function main(){
    UpdateHtml()
    setInterval(UpdateHtml, 1000);
}


