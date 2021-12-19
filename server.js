var express = require('express');
var app = express();
var port = 5005;
const path = require('path');
// const router = express.Router();
app.use(express.static('./'));

// router.get('/',function(req,res){
//   res.sendFile(path.join(__dirname+'/rldemo.html'));
//   //__dirname : It will resolve to your project folder.
// });
// app.use('/', router);
app.listen(port, function () {
  console.log(`Example app listening on port ${port}!`);
});