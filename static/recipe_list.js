$(document).on("click", ".recipe-btn", function(){
    window.location.href = "http://127.0.0.1:5000/" + $(this).attr("id")
})
