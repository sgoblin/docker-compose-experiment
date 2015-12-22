var clickbutton = document.getElementById('clickbutton');

var checkClick = function() {
  var checkClicks = new XMLHttpRequest();
  checkClicks.open("GET", "/increment", "true");
  checkClicks.send();
  checkClicks.onreadystatechange = function() {
    if (checkClicks.readyState == 4) {
      var numClicks = checkClicks.responseText;
      document.getElementById('numclicked').innerHTML = numClicks;
    };
  };
};

clickbutton.addEventListener("click", function(){
  var addClickRequest = new XMLHttpRequest();
  addClickRequest.open("POST", "/increment", "true");
  addClickRequest.send("1");
  checkClick();
});

document.addEventListener('DOMContentLoaded', checkClick);
