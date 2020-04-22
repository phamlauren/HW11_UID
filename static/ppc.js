var display_lists = function(available_ingredients, added_ingredients){
    //empty old data
    $("#available_ingredients").empty()
    $("#added_ingredients").empty()
    //insert all new data
    $.each(available_ingredients, function(i, ingredient){
        var available_ingredient = $("<div>")
        $(available_ingredient).addClass("draggable-employee")
        $(available_ingredient).text(ingredient)
        $(available_ingredient).hover(function(){
            $(this).addClass("hover")
        }, function(){
            $(this).removeClass("hover")
        })
        $("#available_ingredients").append(available_ingredient)
    })

    $.each(added_ingredients, function(i, ingredient){
        var added_ingredient = $("<div>")
        $(added_ingredient).addClass("draggable-committee")
        $(added_ingredient).text(ingredient)
        $(added_ingredient).hover(function(){
            $(this).addClass("hover")
        }, function(){
            $(this).removeClass("hover")
        })
        $("#added_ingredients").append(added_ingredient)
    })

    $("#non-target").droppable({
        accept: ".draggable-committee",
        drop: function(event, ui){
            var name = ui.draggable.text()
            move_to_available_ingredients(name)
            $(ui.draggable).remove()
        }
    })
    $("#ppc-target").droppable({
        accept: ".draggable-employee",
        drop: function(event, ui){
            var name = ui.draggable.text()
            move_to_added_ingredients(name)
            $(ui.draggable).remove()
        }
    })
    $(".draggable-employee").draggable({
        revert: true,
        drag: function(event, ui){
            $(ui.draggable).addClass("hover")
        }
    })
    $(".draggable-committee").draggable({
        revert: true,
        drag: function(event, ui){
            $(ui.draggable).addClass("hover")
        }
    })
}

var move_to_added_ingredients = function(name){
    var data_to_save = {"name": name}
    console.log(name)
    console.log(data_to_save)         
    $.ajax({
        type: "POST",
        url: "move_to_added_ingredients",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var added_ingredients = result["added_ingredients"]
            var available_ingredients = result["available_ingredients"]
            display_lists(available_ingredients, added_ingredients)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var move_to_available_ingredients = function(name){
    var data_to_save = {"name": name}         
    $.ajax({
        type: "POST",
        url: "move_to_available_ingredients",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var added_ingredients = result["added_ingredients"]
            var available_ingredients = result["available_ingredients"]
            display_lists(available_ingredients, added_ingredients)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

$(document).ready(function(){
    display_lists(available_ingredients, added_ingredients)
})