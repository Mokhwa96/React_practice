const express = require('express');
const app = express();

app.use(express.static(__dirname + "/public"));
app.set('port', process.env.PORT || 3000); 
app.get('/', (req, res) => { 
  res.sendFile(__dirname, 'index.html'); 
});
app.listen(app.get('port'), () => {
  console.log(app.get('port'), '번 포트에서 대기 중');
})