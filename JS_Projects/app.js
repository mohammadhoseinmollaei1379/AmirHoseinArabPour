const express = require('express')
const app = express()

const port = 3000
app.listen(port, function(){
    console.log('server is running at http://localhost:' + port)
}) 

app.get('/', function(req, res){
    res.send("aaa.html");
})

app.get('/api/hello/:name', function(req, res){
    let name = req.params.name;
    res.send('hello ' + name);
})