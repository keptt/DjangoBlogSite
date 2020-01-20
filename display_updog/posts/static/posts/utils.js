$(document).ready(function() {

    $('.list-group').children().mouseenter(function() {
        $(this).addClass("active");
    }).mouseleave(function() {
        $(this).removeClass("active");
    });
  });
