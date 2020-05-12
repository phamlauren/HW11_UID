var search_recipes = function(search_string){
    var data = {"search_string": search_string}

    $.ajax({
        type: "POST",
        url: "/search_recipes",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data),
        success: function(result){
        	var status = result["status"]
        	if(status){
            	var recipe_id = result["recipe_id"]
            	window.location.href = "http://127.0.0.1:5000/" + recipe_id
        	}
        	else{
        		alert("We're sorry, we have no drinks with a name that matches your search. Please search another name or select a recipe from the recipe list.")
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
      if(window.location.href.indexOf("recipe_list") > -1){
        $("#list_nav").addClass("active")
        $("#learn_nav").removeClass("active")
        $("#quiz_nav").removeClass("active")
      }
      else if(window.location.href.indexOf("quiz") > -1){
        $("#list_nav").removeClass("active")
        $("#learn_nav").removeClass("active")
        $("#quiz_nav").addClass("active")

      }
      else{
        $("#list_nav").removeClass("active")
        $("#learn_nav").addClass("active")
        $("#quiz_nav").removeClass("active")

      }

      $("#search_input").keyup(function(e){
            if(e.key == "Enter"){
                  var search_string = $("#search_input").val()
                  search_recipes(search_string)
            }
      })

      $("#submit").click(function(){
            var search_string = $("#search_input").val()
            search_recipes(search_string)
      })
})

$(document).on("click", "#learn_link", function(){
	if(window.location.href.indexOf("recipe_list")>-1){
		alert("Please choose a recipe to learn.")
	}
	else{
		// http://127.0.0.1:5000/<int:recipe_id>
		first_digit = window.location.href.charAt(22)
		second_digit = window.location.href.charAt(23)
		console.log(first_digit)
		console.log(second_digit)
		if(second_digit == "/"){
			window.location.href = "http://127.0.0.1:5000/" + first_digit
		}
		else{
			window.location.href = "http://127.0.0.1:5000/" + first_digit + second_digit
		}

	}
})

$(document).on("click", "#quiz_link", function(){
	if(window.location.href.indexOf("recipe_list")>-1){
		alert("Please choose a recipe to take a quiz on.")
	}
	else{
		// http://127.0.0.1:5000/<int:recipe_id>
		first_digit = window.location.href.charAt(22)
		second_digit = window.location.href.charAt(23)
		console.log(first_digit)
		console.log(second_digit)
		if(second_digit == "/"){
			window.location.href = "http://127.0.0.1:5000/" + first_digit + "/quiz_mix"
		}
		else{
			window.location.href = "http://127.0.0.1:5000/" + first_digit + second_digit + "/quiz_mix"
		}

	}
})

$(document).on("click", function() {
    $("#recipe_dropdown").addClass("hide-dropdown");
    $("#pointer").addClass("hide-dropdown");
});

$(document).on("drop", function() {
    $("#recipe_dropdown").addClass("hide-dropdown");
    $("#pointer").addClass("hide-dropdown");
});

$(document).on("click", "#select_dropdown", function(e){
    e.stopPropagation();
    if(window.location.href.indexOf("recipe_list")>-1){
      alert("Please choose a recipe.")
    }
    else{
      if($("#recipe_dropdown").hasClass("hide-dropdown")){
        $("#recipe_dropdown").removeClass("hide-dropdown")
        $("#pointer").removeClass("hide-dropdown")
      }
      else{
      $("#recipe_dropdown").addClass("hide-dropdown")
      $("#pointer").addClass("hide-dropdown")
      }
    }
})
