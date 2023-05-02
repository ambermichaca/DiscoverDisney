
//functions//
function createSearchLink(input){
    window.location.href = "/search_results/" + input
}

function healthCheck(){
    let searchEntry = $.trim($("#search-input").val())
    if (searchEntry == ""){
        console.log("Search was empty")
        reset()
    }
    else {
        createSearchLink(searchEntry)
    }  
}

function reset(){
    $("#search-input").val("")                                           //reset text inside input textbox to 0                                          //return cursor to the input box 
}

$(document).ready(function () { 

    $("#search-button").click(function(){
        console.log("Search-button clicked")
        healthCheck()
    })
    $("#search-input").on('keypress', function(e){                          
        if(e.which == 13){
            console.log("Search-button entered")
            healthCheck()
        }  
    })

})