$(document).ready(function () {
    

    $('.text').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"bounceIn",
        },
        out: {
            effect:"bounce",
        }
    });
    //siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 640,
        height: 150,
        style:"ios9",
        amplitude:"1",
        speed:"0.30",
        autostart:true,
        display:"flex",
        justifycontent:"center",
        alignitems:"center",
        
      });
      // siri messgae animaction
      $('.siri-message').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"fadeInUp",
            sync:true,
        },
        out: {
            effect:"fadeOutUp",
            sync:true,
        }
    });
});