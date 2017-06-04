var request = require('request');
var fs = require('fs');
var prompt = require('prompt')

if(process.argv[2] === 'leaderboard'){
  fs.readFile('data.txt', function(err,data){
    var obj = {}
    var arrData = data.toString().split('\n');
    for(var i = 0; i < arrData.length; i++){
      obj[arrData[i]] = (obj[arrData[i]] || 0) + 1;
    }
    var max = 0;
    var item;
    for(var prop in obj){
      if(obj[prop] > max){
        max = obj[prop];
        item = prop;
      }
    }
    console.log(item);
  })
} else {
  prompt.start()

  var schema = {
    properties: {
      id: {
        description: 'Enter a Pokemon ID',
        pattern: /[0-9]+/,
        message: 'Must be a number',
        required: 'true'
      }
    }
  }

  prompt.get(schema, function (err, result) {
    request('http://pokeapi.co/api/v2/pokemon/'+result.id, function(err,res,data){
      if(!err && res.statusCode == 200){
        data2 = JSON.parse(data);
        fs.appendFile('data.txt',`${data2.forms[0].name[0].toUpperCase()}${data2.forms[0].name.slice(1)}\n`, function(err, data){
          console.log(data2.forms[0].name[0].toUpperCase() + data2.forms[0].name.slice(1))
        })
      }
    })
  });
}


