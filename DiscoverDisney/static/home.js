function create_link(ride) {
    
    let curRide = ride
    let title = curRide["title"]
    let image = curRide["image"]
    let altText = curRide["alt_text"]
    let col = $('<div class="col-md-4"></div>')


    //adjust width NEW 
    let cardContainer = $('<div class="card text-center"> </div>')
    let cardBody = $('<div class="card-body"> </div>')
    let cardText = $('<p class="card-text"> </p>')
    $(cardText).text(title)
    $(cardText).addClass("brown")
    $(cardBody).append(cardText)
    
    let content = $("<a href='/view/" + curRide['id'] + "'><img class = 'card-img-top' src='"+image+"'"+" alt='"+altText+"'" + " width= '100%'></a");
    
    //NEW 
    $(cardContainer).append(content)
    $(cardContainer).append(cardBody)
    $(cardContainer).addClass("cards")
    $(col).append(cardContainer)
    $("#ride-div").append(col) 

}

$(document).ready(function(){
    console.log("make a card")
	create_link(rides["1"])
	create_link(rides["2"])
	create_link(rides["3"])
    create_link(rides["4"])
	create_link(rides["5"])
    create_link(rides["6"])
	create_link(rides["7"])
    create_link(rides["8"])
	create_link(rides["9"])
    create_link(rides["10"])
})
