


(function (window) {
    var speakWord = "Good bye";  
      
    var GoodbyeSpeaker= {};  
    GoodbyeSpeaker.names = ["Yaakov", "John", "Jen", "Jason", "Paul", "Frank", "Larry", "Paula", "Laura", "Jim"]; 
    GoodbyeSpeaker.speak = function  () {
        for (var i = 0; i <  GoodbyeSpeaker.names.length; i++){  
         
        //console.log(speakWord + " " + GoodbyeSpeaker.names[i])
    }
    }
    window.GoodbyeSpeaker = GoodbyeSpeaker;
  
  }) (window)