//Module 4 solution

//Step 1 
 

helloSpeaker.speak ();
GoodbyeSpeaker.speak (); 


(function ( ) { 
    var names = ["Yaakov", "John", "Jen", "Jason", "Paul", "Frank", "Larry", "Paula", "Laura", "Jim"];
     

    for (var i = 0; i < names.length; i++) {
 
    var firstLetter = names[i].charAt(0).toLowerCase();
 
    if (firstLetter === 'j') {
        GoodbyeSpeaker.speak(names[i]);
        console.log("Good bye" + " " + names[i])
         
    } else {
        helloSpeaker.speak(names[i]);
        console.log("Hello" + " " + names[i])
         
    }
    }
      
})( );
 



 


    
 
