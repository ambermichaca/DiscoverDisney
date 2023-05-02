
function displayNameSearchResults(nameResults){
    if (nameResults.length == 0) {
        let row = $('<div class="row"></div>')
        $(row).text("No Matches Found")
        row.addClass("red");      
        $("#search-name-results-div").append(row)
        return
    }
    else{
        $.each(nameResults, function (i, result) {
       
    
            let title = result["title"]
    
            let col = $('<div class=""></div>')

            let content = $("<a href='/view/" + result['id'] + "'>"); 
            $(content).text(title)
            content.addClass("darkblue");   
            $(col).append(content);
            $("#search-name-results-div").append(col)

    
        })
    }
}


function displayNeighborhoodSearchResults(neighborhoodResults){
    console.log(neighborhoodResults)
    if (neighborhoodResults.length == 0) {
        let row = $('<div class="row"></div>')
        $(row).text("No Matches Found")
        row.addClass("red");      
        $("#search-neighborhood-results-div").append(row)
        return
    }
    else{
        $.each(neighborhoodResults, function (i, result) {

            let title = result["title"]
            let neighborhood = result["neighborhood"]
    
            let col = $('<div class=""></div>')

            let content = $("<a href='/view/" + result['id'] + "'>"); 
            $(content).text(title + ": " + neighborhood)
            $(col).append(content);
            $("#search-neighborhood-results-div").append(col)

    
        })
    }
}

function displayAccesibilitySearchResults(accesibilityResults){
    
    
    if (accesibilityResults.length == 0) {
        let row = $('<div class="row"></div>')
        $(row).text("No Matches Found")
        row.addClass("red");      
        $("#search-accesibility-results-div").append(row)
        return 
    }
    else{
        $.each(accesibilityResults, function (i, result) {

            let title = result["title"]
            let accesibilityItems = result["accesibility"]
            let matches = [];
            

            $.each(accesibilityItems, function (i, item) {
                if (item.toLowerCase().indexOf(searchString.toLowerCase()) >= 0){
                    matches.push(item)
        
                }
                
            })
            let col = $('<div class=""></div>')
            let content = $("<a href='/view/" + result['id'] + "'>");
            $(content).text(title + ": " + matches.toString())
            $(col).append(content);
            $("#search-accesibility-results-div").append(col)
        })
        
        
    }
}








$(document).ready(function () {
    displayNameSearchResults(nameResults)
    displayNeighborhoodSearchResults(neighborhoodResults)
    displayAccesibilitySearchResults(accesibilityResults)
})