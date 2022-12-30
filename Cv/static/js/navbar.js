var style={
    color:" #FFDB70",
}


$( function() {
    $( ".navbar li .nav-item" ).click(function(){
        $(".navbar li a").css(style)
    });
  } );