var display_lists = function(recipe, available_ingredients, added_ingredients){
    //empty old data
    $("#recipe-instructions").empty()
    $("#available-ingredients").empty()
    $("#added-ingredients").empty()
    //insert all new data

    $("#ppc-target").attr("data-id", recipe["id"])
    $.each(recipe["garnish_ingredients"], function(i, item){
        var list_item = $("<div>")
        $(list_item).addClass("list-item")
        if((item.amount == item.amount_added) || (item.amount == null && added_ingredients.some(function(element){return element.quiz_id === item.quiz_id}))){
            $(list_item).addClass("completed-item")
        }
        if(item.unit == ""){
            $(list_item).text(item.ingredient)
        }
        else if(item.amount == null){
            $(list_item).text(item.ingredient + "," + item.unit)
        }
        else{
            $(list_item).text(item.ingredient + ", " + item.amount + item.unit)

        }
        $("#recipe-instructions").append(list_item)
    })
 
    if(available_ingredients.length < 1){
        var success_message = $("<div>")
        $(success_message).text("Congratulations! You've successfully made a " + recipe["name"] + ".")
        $("#available-ingredients").append(success_message)
    }
    else{
        $.each(available_ingredients, function(i, ingredient){
            var available_ingredient = $("<div>")
            $(available_ingredient).addClass("draggable-employee")
            $(available_ingredient).attr("data-id", ingredient.quiz_id)
            if(ingredient.unit == ""){
                $(available_ingredient).text(ingredient.ingredient)
            }
            else if(ingredient.amount == null){
                $(available_ingredient).text(ingredient.ingredient + "," + ingredient.unit)
            }
            else{
                $(available_ingredient).text(ingredient.ingredient + ", " + "1" + ingredient.unit)
            }
            $(available_ingredient).hover(function(){
                $(this).addClass("hover")
            }, function(){
                $(this).removeClass("hover")
            })
            $("#available-ingredients").append(available_ingredient)
        })
    }

    $.each(added_ingredients, function(i, ingredient){
        console.log(added_ingredients)
        var added_ingredient = $("<div>")
        $(added_ingredient).addClass("draggable-committee")
        $(added_ingredient).attr("data-id", ingredient.quiz_id)
        if(ingredient.unit == ""){
            $(added_ingredient).text(ingredient.ingredient)
        }
        else if(ingredient.amount == null){
            $(added_ingredient).text(ingredient.ingredient + "," + ingredient.unit)
        }
        else{
            $(added_ingredient).text(ingredient.ingredient + ", " + ingredient.amount_added + ingredient.unit)
        }
        $(added_ingredient).hover(function(){
            $(this).addClass("hover")
        }, function(){
            $(this).removeClass("hover")
        })
        $("#added-ingredients").append(added_ingredient)
    })

    $("#non-target").droppable({
        accept: ".draggable-committee",
        drop: function(event, ui){
            var ingredient_id = ui.draggable.data("id")
            var recipe_id = $("#ppc-target").data("id")
            move_to_available_ingredients(ingredient_id, recipe_id)
            $(ui.draggable).remove()
        }
    })
    $("#ppc-target").droppable({
        accept: ".draggable-employee",
        drop: function(event, ui){
            var ingredient_id = ui.draggable.data("id")
            var recipe_id = $("#ppc-target").attr("data-id")
            console.log(ingredient_id)
            console.log(recipe_id)
            move_to_added_ingredients(ingredient_id, recipe_id)
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

var move_to_added_ingredients = function(ingredient_id, recipe_id){
    var data_to_save = {"ingredient_id": ingredient_id, "recipe_id": recipe_id} 
    $.ajax({
        type: "POST",
        url: "add_to_shaker",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var recipe = result["recipe"]
            var added_ingredients = result["added_ingredients"]
            var available_ingredients = result["available_ingredients"]
            display_lists(recipe, available_ingredients, added_ingredients)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var move_to_available_ingredients = function(ingredient_id, recipe_id){
    var data_to_save = {"ingredient_id": ingredient_id, "recipe_id": recipe_id}         
    $.ajax({
        type: "POST",
        url: "remove_from_shaker",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var recipe = result["recipe"]
            var added_ingredients = result["added_ingredients"]
            var available_ingredients = result["available_ingredients"]
            display_lists(recipe, available_ingredients, added_ingredients)
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
    display_lists(recipe, available_ingredients, added_ingredients)
})