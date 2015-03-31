jQuery(window).load(function() {
    $(".navbar-toggle").click(function() {
        $("#portal-globalnav").slideToggle(500);
        $("#portal-megamenu").toggleClass("open");
    });
    $("#portal-globalnav li .subs").parent("#portal-globalnav li").addClass("plus");
    $("#portal-globalnav > li.plus > a").click(function(event) {
        if ($(window).width() <= 768) {
            event.preventDefault();
            $("#portal-globalnav > li").not($(this).parent()).removeClass("open").find(".subs").slideUp(350);
            $(this).parent().toggleClass("open").find(".subs").slideToggle(500);
        }
    });
});
