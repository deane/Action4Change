// Javascript function for BTC website

//move backwards thanks to the left arrow

function moveLeft(){

}

//move forward thanks to the right arrows

function moveRight(){

}

//did it button, post action on facebook

function didIt(id){
    console.log("post a did it action");
         console.log("url_art: "+id);
         FB.api('/me/btcinteract:complete', 'post', {challenge :'http://btcinteract.com/day/'+id+'/'}, function(response){
                  if( !response || response.error){
                         console.log("error....");
                    } else {
                         console.log("Your trip has been post succesfully! Post ID: "+response.id);

                   };
                 });
}

//challenge a friend function 

function challengeAFriend(theme){
 FB.ui({
          method: 'send',
          name: theme,
          link: 'http://btcinteract.com',
          });
}

// share on facebook function 

function fbShare(){
 
}

//post on tweeter

function tweet(id){

}


//logout function 

function fbLogout(){
   FB.logout(function(response) {
  // user is now logged out
});
}
