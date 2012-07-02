// Javascript function for BTC website


//move backwards thanks to the left arrow

function getMail(){
var email;
FB.api('/me', function(response) {
   email =  response.email;
   console.log(email);
   $.ajax({url: 'http://challenges4change.org/mail/?mail='+email,context: document.body});
    });
}

//move forward thanks to the right arrows

function moveRight(){

}

//did it button, post action on facebook

function didIt(year, month, day){
    console.log("post a did it action");
        if(FB.getUserID() == '0'){
		FB.login(function(response) {
   if (response.authResponse) {
     console.log('Welcome!  Fetching your information.... ');
     FB.api('/me', function(response) {
  FB.api('/me/btcinteract:complete', 'post', {challenge :'http://challenges4change.org/day/'+year+'/'+month+'/'+day+'/'}, function(response){
                  if( !response || response.error){
                         console.log("error....");
                    } else {
                         console.log("Your trip has been post succesfully! Post ID: "+response.id);

                   };
                 });      
 console.log('Good to see you, ' + response.name + '.');
     });
   }                   

 });
};
         FB.api('/me/btcinteract:complete', 'post', {challenge :'http://challenges4change.org/day/'+year+'/'+month+'/'+day+'/'}, function(response){
                  if( !response || response.error){
                         console.log("error....");
                    } else {
                         console.log("Your trip has been post succesfully! Post ID: "+response.id);

                   };
                 });
}

//challenge a friend function 

function challengeAFriend(theme, year, month, day){
 FB.ui({
          method: 'send',
          name: theme,
          link: 'http://challenges4change.org/day/'+year+'/'+month+'/'+day,
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
document.getElementById('logout').style.display='none';
document.getElementById('login').style.display='';
}


function fbLogin(){
document.getElementById('login').style.display='none';
document.getElementById('logout').style.display='';
}
