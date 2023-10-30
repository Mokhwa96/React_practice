const express = require('express');
const app = express();
const spawn = require('child_process').spawn; 
app.set('port', process.env.PORT || 3000); 
app.get('/', (req, res) => { 
  const py_process = spawn('python', ['test.py']) 
  py_process.stdout.on('data', function(data){ 
    console.log(data.toString());
    res.send(data.toString());
  });

  py_process.stderr.on('data', function(data){ 
    console.log(data.toString());
  });
});
app.listen(app.get('port'), () => {
  console.log(app.get('port'), '번 포트에서 대기 중');
})