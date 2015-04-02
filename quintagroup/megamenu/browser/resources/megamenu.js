jQuery(window).load(function() {
    $(".navbar-toggle").click(function() {
        $(".megamenu-nav").slideToggle(500);
        $("#portal-megamenu").toggleClass("open");
    });
    $(".megamenu-nav li .subs").parent(".megamenu-nav li").addClass("plus");
    $(".megamenu-nav > li.plus > a").click(function(event) {
        if ($(window).width() <= 768) {
            if ($(this).parent().is(':not(.open)')) {
                event.preventDefault();
                $(".megamenu-nav > li").not($(this).parent()).removeClass("open").find(".subs").slideUp(350);
                $(this).parent().toggleClass("open").find(".subs").slideToggle(500);
            }
        }
    });
    $(window).resize(function() {
        if ($(window).width() >= 768) {
            $(".megamenu-nav").css({'display': 'block'})
            $(".megamenu-nav .subs").removeAttr('style');
        } else {
            $("#portal-megamenu:not(.open) .megamenu-nav").css({'display': 'none'})
        }
    });
});
