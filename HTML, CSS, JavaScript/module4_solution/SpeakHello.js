//SpeakHello object




(function (window) { 
  var speakWord = "Hello"; 
   
  var helloSpeaker= {};  
  helloSpeaker.names = ["Yaakov", "John", "Jen", "Jason", "Paul", "Frank", "Larry", "Paula", "Laura", "Jim"]; 
  helloSpeaker.speak = function  () {
    for (var i = 0; i < helloSpeaker.names.length; i++){  
    //console.log(speakWord + " " + helloSpeaker.names[i])
  } 
  }  
 
  window.helloSpeaker = helloSpeaker;

})(window)




