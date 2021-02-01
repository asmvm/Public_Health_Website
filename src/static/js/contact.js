// Emergency hotline & contact information: 

// Getting a reference to the button on the page with the id property set to `click-me`
var button = d3.select("#reveal-me");


// This function is triggered when the button is clicked
function handleClick(button_id) {
    var button_id = 
    reveal_more(button_id);

  // We can use d3 to see the object that dispatched the event
  console.log(d3.event.target);
}

// We can use the `on` function in d3 to attach an event to the handler function
button.on("click", handleClick);

// You can also define the click handler inline
button.on("click", function() {
  console.log("Hi, a button was clicked!");
  console.log(d3.event.target);
});

// On click button to reveal emeregency contact information: 
function reveal_more ( element_to_show ) {
    var element_to_show = getRefToDiv( element_to_show );
    element_to_show.style.display = "inline";
    }

// Forms for contact information & inquiries: 

// Getting a reference to the input element on the page with the id property set to 'input-field'
var inputField = d3.select("#input-field");