var category = {category};
console.log(category);
//  for(var i = 0; i < document.querySelectorAll("img").length - 2; i++){
//     var imgNumber = i + 1; 
//      document.querySelectorAll("img")[i].src("./images/all/pic" + imgNumber + ".png");
//  }

var buttons =  [];

$("#ai-demo").click(function(){
    $(".value-1").addClass("effect");
})


console.log("hello world");

$.getJSON("./stuff.json", function(json) {
    console.log(json); // this will show the info it in firebug console
});

fetch('/').then(function(response){
    return response.json();
}).then(function(obj){
    console.log(obj);
}).catch(function(error){
    console.error("dawda")
});

