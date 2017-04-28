## Iterators More Exercises
### Part I

Write a function called `printEmails` which console.log's each email for the users.

```javascript
function printEmails(){
	users.forEach(function(val){
		console.log(val.email);
    })
}
```

Write a function called `printHobbies` which console.log's each hobby for each user.

```javascript
function printHobbies(){
	users.forEach(function(val){
		val.hobbies.forEach(function(val2){
			console.log(val2);
        })
    })
}
```

Write a function called `findHometownByState` which returns the first user which has a hometown of the state that is passed in

```javascript
function findHometownByState(key){
	console.log(users.find(function(val){
		return val.hometown.state === key;
    }));
}
```
