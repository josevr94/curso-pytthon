$(document).ready(function () {
    $("#changeTexButton").click(function () {
        $("#paragraph").text("----------texto cambiado----------");
    });
    $("#parrafo2").mouseover(function () {
        $(this).css("background-color", "red");
    });
    $("#parrafo2").mouseout(function () {
        $(this).css("background-color", "white");
    });
    $("#animarCaja").click(function () {
        $("#box").animate({
            width: "100px",
            height: "100px",
            opacity: 0.5
        }, 1000);
    });
    $("#animarCaja").dblclick (function () {
        $("#box").animate({
            width: "200px",
            height: "200px",
            opacity: 1
        }, 1000);
    });
    
});