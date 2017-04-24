# _Iterators_


## .forEach Exercises


Write a function called `printFirstAndLast` which accepts an array (of objects) and console.logs a new string with the first character and the last character of each value.

```javascript

function printFirstAndLast(arr){
	arr.forEach(function(val,index){
		console.log(val[0] + val[arr[index].length-1]);
    });
}

printFirstAndLast(['awesome','example','of','forEach']);

//ae
//ee
//of
//fh
```

Write a function called `addKeyAndValue` which accepts three parameters, an array (of objects), a key and a value. This function should return the array of objects after each key and value have been added to each object in the array.

```javascript
function addKeyAndValue(arr, key, bol){
	arr.forEach(function(val){
		val[key] = bol;
    });
	console.log(arr);
}

addKeyAndValue([{name: 'Elie'},{name: 'Tim'},{name: 'Elie'}], "isInstructor", true) 

/*
[
    {
        name: 'Elie',
        isInstructor: true
    },
    {
        name: 'Tim',
        isInstructor: true
    },
    {
        name: 'Elie',
        isInstructor: true
    }
]
*/


```
## .map Exercises

Write a function called `valTimesIndex` which accepts an array of numbers and returns a new array with each value multiplied by the index it is at in the array:  

```javascript
function valTimesIndex(arr){
	return arr.map(function(val,index){
		return val * index;	
    });
}

valTimesIndex([1,2,3]) // [0,2,6]
valTimesIndex([5,10,15]) // [0,10,30]
```

Write a function called `extractKey` which accepts two parameters, an array of objects, and the name of a key and returns an array with just the values for that key:  

```javascript
function extractKey(arr, key){
    return arr.map(function(arr){
		return arr.key;
    })
}

extractKey([{name: "Elie", isInstructor:true},{name: "Tim", isInstructor:true},{name: "Matt", isInstructor:true}], "name")

// ["Elie", "Tim", "Matt"]
```

## .filter Exercises
Write a function called `filterLetters` which accepts an array of letters and returns the number of occurrences of a specific letter. This function should be case **insensitive**

```javascript
function filterLetters(arr, key){
	return arr.filter(function(arr){
		return arr.toLowerCase() === key.toLowerCase()
    }).length
}

filterLetters(["a","a","b","c","A"], "a"); // 3
filterLetters(["a","a","b","c","A"], "z"); // 0
filterLetters(["a","a","b","c","A"], "B"); // 1
```

Write a function called `filterKey` which accepts two parameters, an array of objects, and the name of a key and returns an array with only those objects which have truthy values for that key:

```javascript
function filterKey(arr,key){
	return arr.filter(function(arr){
		return arr[key] === true;
    })
}

JSON.stringify(filterKey([{name: "Elie", isInstructor:true, isHilarious: false},{name: "Tim", isInstructor:true, isHilarious: true},{name: "Matt", isInstructor:true}], "isHilarious"));

filterKey([{name: "Elie", isInstructor:true, isHilarious: false},{name: "Tim", isInstructor:true, isHilarious: true},{name: "Matt", isInstructor:true}], "isHilarious")

// [{name: "Tim", isInstructor:true, isHilarious:true}]
```

## .reduce Exercises

Write a function called `extractKey` which accepts two parameters, an array of objects, and the name of a key and returns an array with just the values for that key:

```javascript
function extractKey(arr, key){
	return arr.reduce(function(acc,nextVal,i){
		acc.push(nextVal.name);
		return acc;
    },[]);
}

extractKey([{name: "Elie", isInstructor:true},{name: "Tim", isInstructor:true},{name: "Matt", isInstructor:true}], "name");

// ["Elie", "Tim", "Matt"]
```

Write a function called `filterLetters` which accepts an array of letters and returns the number of occurrences of a specific letter. This function should be case **insensitive**

```javascript
function filterLetters(arr,key){
	return arr.reduce(function(acc,val){
		if(val.toLowerCase() === key.toLowerCase()){
			console.log(acc++);
			console.log(++acc);
			return ++acc;
        } else {
			return acc;
        } 
    },0);	
}

filterLetters(["a","a","b","c","A"], "a"); // 3
filterLetters(["a","a","b","c","A"], "z"); // 0
filterLetters(["a","a","b","c","A"], "B"); // 1
```

Optional Bonus

Write a function called `addKeyAndValue` which accepts three parameters, an array (of objects), a key and a value. This function should return the array of objects after each key and value has been added. You can do this a few ways, either by reducing starting with an empty array and making copies of the object or by starting with the actual array!


```javascript
function addKeyAndValue(arr, key, bol){
	return arr.reduce(function(acc,next){
		var newObj = {};
		newObj.name = next.name;
		newObj[key] = bol;
		console.log(newObj);
		return acc.concat(newObj);
    },[]);
}

addKeyAndValue([{name: 'Elie'},{name: 'Tim'},{name: 'Elie'}], "isInstructor", true);

/*
[
    {
        name: 'Elie',
        isInstructor: true
    },
    {
        name: 'Tim',
        isInstructor: true
    },
    {
        name: 'Elie',
        isInstructor: true
    }
]
*/
```