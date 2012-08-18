// Javascript functions for BTC website
// check email format

function isValidEmailAddress(emailAddress) {
	var re =/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return re.test(emailAddress);
}

//move backwards thanks to the left arrow

function subscribe(){
	var email = 'null';
	email = document.getElementById('email').value;
	console.log("Desktop email: " + email);
	if(email== ''){
		email = document.getElementById('email_mobile').value;
		console.log("Mobile email: " + email);
	} if(email=='') {
		email = document.getElementById('email_tablet').value;
		console.log("Tablet email: " + email_tablet);
	}

if(isValidEmailAddress(email) ){
   $.get('http://challenges4change.org/mail/?mail='+email,
         function(data){
		console.log(data);
		$('#alert-message').html(data);
		$('#alert-message-mobile').html(data);
		_gaq.push(['_trackEvent','Social','Subscribed','Email']);
	},
	"html")
/*   $.ajax({url: 'http://challenges4change.org/mail/?mail='+email,
           context: document.body,
           sucess : foundation_alert
          });*/
} else {
alert("Your email address is not correct..")
}
}

// Unsubscribe function 

function unsubscribe(){
	var email = document.getElementById('email').value;
	if(email ==''){
		email = document.getElementById('email_mobile').value;
	} if(email=='') {
		email = document.getElementById('email_tablet').value;
		console.log("Tablet email: " + email_tablet);
	}
	if(isValidEmailAddress(email)){
   		$.get('http://challenges4change.org/mail/un/?mail='+email,
         		function(data){
			console.log(data);
			$('#alert-message').html(data);
			$('#alert-message-mobile').html(data);
			},
		"html")
/*   $.ajax({url: 'http://challenges4change.org/mail/?mail='+email,
           context: document.body,
           sucess : foundation_alert
          });*/
   	} else { 
		alert("Your email address is not correct.")
	}	
}

/*
 * Challenges4Change Overlay Javascript
 */

function closeOverlay() {
        document.body.removeChild(document.getElementById('overlay'));
        document.body.removeChild(document.getElementById('grayout'));
}

function createOverlay(extraClasses) {
        var overlay = document.getElementById('overlay');
        if(overlay != null)
                closeOverlay();

        var grayout = document.createElement('a');
        var grayoutDiv = document.createElement('div');
        grayout.setAttribute('href', 'javascript: closeOverlay()');

        grayout.setAttribute('id', 'grayout');
        grayoutDiv.setAttribute('class', 'grayout');
        grayout.appendChild(grayoutDiv);
        document.body.appendChild(grayout);

        overlay = document.createElement('div');
        overlay.setAttribute('id', 'overlay');

        var overlayClass = 'overlay';
        if(typeof(extraClasses) != 'undefined')
                overlayClass += ' '+ extraClasses;
        overlay.setAttribute('class', overlayClass);

        document.body.appendChild(overlay);

        // add close button
        var btn = document.createElement('a');
        btn.setAttribute('href', 'javascript: closeOverlay()');
        btn.setAttribute('class', 'close-button ir');
        var span = document.createElement('span');
        btn.appendChild(span);
        overlay.appendChild(btn);

        return overlay;
}

function popupOffer(label, content){
        var overlay = createOverlay('content-overlay');
        var title = document.createElement('h4');
        title.appendChild(document.createTextNode(label));
        overlay.appendChild(title);

        var div = document.createElement('div');
        div.innerHTML = content;

        overlay.appendChild(div);
}


function startOverlay(url_img){
	if(getCookie('start') == 'true'){
		return;
	} else {
		var info = '<div class="spaced_overlay"><a href="http://bit.ly/c4c-igg" onclick="javascript:closeOverlay()" target="_blank"><img src="http://challenges4change.org/static/images/C4ConIndiegogo.png" /></a></div>';
		popupOffer('Please help support this project. Go to our fundraising campaign to contribute: ', info);
		setCookie('start', 'true');	
	}
}

/**
 * Set and Get cookie
 */

// fucnton which creat a cookie 

function setCookie(c_name,value){
        var c_value=escape(value);
        document.cookie=c_name + "=" + c_value + "; path=/";
}


// funcuton which get a cookie 

function getCookie(c_name){
        var i,x,y,ARRcookies=document.cookie.split(";");
        for (i=0;i<ARRcookies.length;i++){
                 x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
                 y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
                 x=x.replace(/^\s+|\s+$/g,"");
                 if (x==c_name){
                     return unescape(y);
                }
        }
}

/* All different facebook function */

//challenge a friend function 

function challengeAFriend(theme, year, month, day){
 FB.ui({
          method: 'send',
          name:"Daily Challenge: " + theme,
          link: 'http://challenges4change.org/day/'+year+'/'+month+'/'+day,
          });
	_gaq.push(['_trackEvent', 'Social', 'Challenge Friends Post']);
}


//initialisation of facebook
function fbInit(){

  FB.init({ appId: '304310869661159' , status: true, cookie: true, xfbml: false});
    fbInitializedCallback();
    name = getName();
}


// facebook feed dialog for the I Dit It button 
function postToFeed(url, img, theme, challenge) {

	FB.init({ appId: '304310869661159' , status: true, cookie: true, xfbml: false});
	name = getName();
	console.log("Name is: " + name);
	if(challenge.length > 145) {
 	   challenge = challenge.substring(0,144)+"...";
	}
        // calling the API ...
        var obj = {
          method: 'feed',
          link: url,
          picture: img,
          name: name + ' completed a Daily Challenge.',
          caption: 'Challenge Theme: ' + theme,
          description: challenge
        };

        function callback(response) {
          console.log("Post ID: " + response['post_id']);
	  _gaq.push(['_trackEvent','Social','I Did It Post']);
        }

        FB.ui(obj, callback);
}

// function which return the first name

function getName(){
  FB.api('/me', function(response){name=response.first_name});
  console.log(name);
  return name;
}

