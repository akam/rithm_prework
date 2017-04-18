window.onload = function(){
	var change = document.querySelector("#change_heading");
	change.innerText = "Hello World!"
	var brown = document.querySelector(".brown");
	var green = document.querySelector(".green");
	var blue = document.querySelector(".blue");
	var yellow = document.querySelector(".yellow");
	var selected = document.querySelector(".selected");
	var purple = document.createElement("div");
	var section = document.querySelector("section");
	var startButton = document.querySelector("button");
	var car1 = document.querySelector(".car1");
	var car2 = document.querySelector(".car2");
	car1.style.marginLeft = 0;
	car2.style.marginLeft = 0;
	var carWidth = 50;
	//Part 1
	brown.addEventListener("mouseover", function(){
		selected.innerText = "brown";
	})
	green.addEventListener("mouseover", function(){
		selected.innerText = "green";
	})
	yellow.addEventListener("mouseover", function(){
		selected.innerText = "yellow";
	})
	blue.addEventListener("mouseover", function(){
		selected.innerText = "blue";
	})
	purple.style.backgroundColor = "purple";
	section.appendChild(purple);
	//Part 2
	startButton.addEventListener("click", function(){
		var race = setInterval(function(){
    		car1.style.marginLeft = parseInt(car1.style.marginLeft) + Math.random() * 10 + "px";
    		car2.style.marginLeft = parseInt(car2.style.marginLeft) + Math.random() * 10 + "px";
    	if(parseInt(car1.style.marginLeft) >= window.innerWidth - carWidth ||
    		parseInt(car2.style.marginLeft) >= window.innerWidth - carWidth){
			clearInterval(race);	
			if(parseInt(car1.style.marginLeft) > parseInt(car2.style.marginLeft)){
				alert("Car 1 is the winner!");
			} else {
				alert("Car 2 is the winner!");
			}
			car1.style.marginLeft = 0;
			car2.style.marginLeft = 0;
		}
		},10);
	})
}