var display_lists = function(recipe, available_ingredients, added_ingredients){
    //empty old data
    $("#available-ingredients").empty()
    $("#added-ingredients").empty()
    //insert all new data

    $("#progress-bar").attr("aria-valuenow", 100*(recipe["progress"]/recipe["until_complete"]))
    $("#progress-bar").css("width", (100*(recipe["progress"]/recipe["until_complete"]) + "%"))

    $("#ppc-target").attr("data-id", recipe["id"])

    $.each(available_ingredients, function(i, ingredient){
        var available_ingredient = $("<div>")
        $(available_ingredient).addClass("draggable-employee")
        $(available_ingredient).attr("data-id", ingredient.quiz_id)
        $(available_ingredient).attr("data-validity", ingredient.quiz_correct)
        $(available_ingredient).attr("data-name", ingredient.ingredient)
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

    $.each(added_ingredients, function(i, ingredient){
        var added_ingredient = $("<div>")
        $(added_ingredient).addClass("draggable-committee")
        $(added_ingredient).attr("data-id", ingredient.quiz_id)
        $(added_ingredient).attr("data-name", ingredient.ingredient)
        if(ingredient.quiz_correct == false){
            $("#instructions-div").text("Oops! The ingredients in the shaker are not quite right. Please drag the incorrect items out - consult the \"Recipe peek\" tool above if you need a reminder!")
            $("#instructions-div").removeClass("hide-media")
            $("#instructions-div").removeClass("short")
            $("#instructions-div").addClass("long")
            $("#reverse-arrow-gif").removeClass("hide-media")
            $("#progress-bar").attr("aria-valuenow", 100*((recipe["progress"]-1)/recipe["until_complete"]))
            $("#progress-bar").css("width", (100*((recipe["progress"]-1)/recipe["until_complete"]) + "%"))

        }
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
            var recipe_id = $("#ppc-target").attr("data-id")
            move_to_available_ingredients(ingredient_id, recipe_id)
            $(ui.draggable).remove()
        }
    })
    $("#ppc-target").droppable({
        accept: ".draggable-employee",
        drop: function(event, ui){
            var ingredient_id = ui.draggable.data("id")
            var recipe_id = $("#ppc-target").attr("data-id")
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
            $("#instructions-div").addClass("hide-media")
            $("#reverse-arrow-gif").addClass("hide-media")
            $("#cursor-gif").addClass("hide-media")
            display_lists(recipe, available_ingredients, added_ingredients)
            if(recipe["progress"] == recipe["until_complete"] && recipe["mix_ingredients"].length == added_ingredients.length){
                $("#arrow-gif").addClass("hide-media")
                $("#shaker-gif").removeClass("hide-media")
                setTimeout(() => { window.location.href = "http://127.0.0.1:5000/" + recipe["id"] + "/quiz_garnish" }, 3500);   
            }
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
            $("#instructions-div").addClass("hide-media")
            $("#reverse-arrow-gif").addClass("hide-media")
            display_lists(recipe, available_ingredients, added_ingredients)
            if(recipe["progress"] == recipe["until_complete"] && recipe["mix_ingredients"].length == added_ingredients.length){
                $("#arrow-gif").addClass("hide-media")
                $("#shaker-gif").removeClass("hide-media")
                setTimeout(() => { window.location.href = "http://127.0.0.1:5000/" + recipe["id"] + "/quiz_garnish" }, 3500);   
            }
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
    $("#recipe_dropdown").empty()
    var recipe_name = $("<div>")
    recipe_name.addClass("recipe-name")
    recipe_name.text(recipe.name)
    $("#recipe_dropdown").append(recipe_name)
    $.each(recipe["mix_ingredients"], function(i, item){
        var list_item = $("<div>")
        if(item.unit == ""){
            $(list_item).text(item.ingredient)
        }
        else if(item.amount == null){
            $(list_item).text(item.ingredient + "," + item.unit)
        }
        else{
            $(list_item).text(item.ingredient + ", " + item.amount + item.unit)   
        }
        $("#recipe_dropdown").append(list_item)
    })
    $("#recipe_dropdown").append("<br />")
    $("#recipe_dropdown").append("<div class=\"recipe-name\">Garnishes</div>")
    $.each(recipe["garnish_ingredients"], function(i, item){
        var list_item = $("<div>")
        if(item.unit == ""){
            $(list_item).text(item.ingredient)
        }
        else if(item.amount == null){
            $(list_item).text(item.ingredient + "," + item.unit)
        }
        else{
            $(list_item).text(item.ingredient + ", " + item.amount + item.unit)   
        }
        $("#recipe_dropdown").append(list_item)
    })
})