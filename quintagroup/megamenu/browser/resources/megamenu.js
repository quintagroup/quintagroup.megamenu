jQuery(window).load(function() {

	$( ".navbar-toggle" ).click(function() {
			$( "#nav" ).slideToggle(500)
            $( "[id$='globalnav']" ).toggleClass( "open" );
		});

    $( "#nav li .subs").has( "ol" ).parent("#nav li").addClass("plus");

    $("#nav > li.plus > a").click(function (event) {
        if ($(window).width() <= 768){
            event.preventDefault();
            $("#nav > li").not($(this).parent()).removeClass("open").find(".subs").slideUp(350);
            $(this).parent().toggleClass("open").find(".subs").slideToggle(500);
            }
        });
    });
