$( "#search" ).submit(function( event ) {
  searchString = $("#search-input").val();
  var response =  $.ajax({
    url: "getInfo/?query=" + searchString,
    method: "POST",
    success: function(responsedata) {
     console.log(responsedata);
     $('#result > div > h1').text(responsedata['query']);
     $('#result > div > p').text(responsedata['answer']);
     $('#result > a').attr('href', responsedata['link']);
    }
  });
  event.preventDefault();
});