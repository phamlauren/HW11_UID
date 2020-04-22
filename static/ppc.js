var display_lists = function(non_ppc, ppc){
    //empty old data
    $("#non-ppc-members").empty()
    $("#ppc-members").empty()
    //insert all new data
    $.each(non_ppc, function(i, person){
        var render_employee = $("<div>")
        $(render_employee).addClass("draggable-employee")
        $(render_employee).text(person)
        $(render_employee).hover(function(){
            $(this).addClass("hover")
        }, function(){
            $(this).removeClass("hover")
        })
        $("#non-ppc-members").append(render_employee)
    })

    $.each(ppc, function(i, committee_member){
        var render_committee_member = $("<div>")
        $(render_committee_member).addClass("draggable-committee")
        $(render_committee_member).text(committee_member)
        $(render_committee_member).hover(function(){
            $(this).addClass("hover")
        }, function(){
            $(this).removeClass("hover")
        })
        $("#ppc-members").append(render_committee_member)
    })

    $("#non-target").droppable({
        accept: ".draggable-committee",
        drop: function(event, ui){
            var name = ui.draggable.text()
            move_to_non_ppc(name)
            $(ui.draggable).remove()
        }
    })
    $("#ppc-target").droppable({
        accept: ".draggable-employee",
        drop: function(event, ui){
            var name = ui.draggable.text()
            move_to_ppc(name)
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

var move_to_ppc = function(name){
    var data_to_save = {"name": name}
    console.log(name)
    console.log(data_to_save)         
    $.ajax({
        type: "POST",
        url: "move_to_ppc",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var ppc = result["ppc_people"]
            var non_ppc = result["non_ppc_people"]
            display_lists(non_ppc, ppc)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var move_to_non_ppc = function(name){
    var data_to_save = {"name": name}         
    $.ajax({
        type: "POST",
        url: "move_to_non_ppc",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var ppc = result["ppc_people"]
            var non_ppc = result["non_ppc_people"]
            display_lists(non_ppc, ppc)
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
    display_lists(non_ppc, ppc)
})