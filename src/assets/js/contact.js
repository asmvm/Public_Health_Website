// Emergency hotline & contact information: 

// // Getting a reference to the button on the page with the id property set to `click-me`
// var button = d3.select("#reveal-me");


// // This function is triggered when the button is clicked
// function handleClick(button_id) {
//     var button_id = 
//     reveal_more(button_id);

//   // We can use d3 to see the object that dispatched the event
//   console.log(d3.event.target);
// }

// // We can use the `on` function in d3 to attach an event to the handler function
// button.on("click", handleClick);

// // You can also define the click handler inline
// button.on("click", function() {
//   console.log("Hi, a button was clicked!");
//   console.log(d3.event.target);
// });

// // On click button to reveal emeregency contact information: 
// function reveal_more ( element_to_show ) {
//     var element_to_show = getRefToDiv( element_to_show );
//     element_to_show.style.display = "inline";
//     }

// // Forms for contact information & inquiries: 

// // Getting a reference to the input element on the page with the id property set to 'input-field'
// var inputField = d3.select("#input-field");

// function revealMore() {
//   var c = document.getElementById("callus");
//   var e = document.getElementById("emailus");
//   var v = document.getElementById("visitus");
//   var h = document.getElementById("helpus");
//   if (c.style.display === "none") {
//     c.style.display = "block";
//   } 
//   if (e.style.display === "none") {
//     e.style.display = "block";
//   } 
//   if (v.style.display === "none") {
//     v.style.display = "block";
//   } 
//   if (h.style.display === "none") {
//     h.style.display = "block";
//   } 
//   else {
//     x.style.display = "none";
//   }
// }

    $(function() {
        $('div.icon-tab').click(function() {
            $(this).addClass('active').siblings().removeClass('active');
            setDisplay(450);
        });

        function setDisplay(time) {
            $('div.icon-tab').each(function(rang) {
                $('.item').eq(rang).css('display', 'none');

                if($(this).hasClass('active')){
                    $('.item').eq(rang).fadeIn(time);
                }
            });
        }

        //Disable the animation on page load
        setDisplay(0);
    });