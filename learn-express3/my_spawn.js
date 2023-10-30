const spawn = require('child_process').spawn; 
const py_process = spawn('python', ['test.py']); 
py_process.stdout.on('data', function(data){ 
  console.log(data.toString());
});
py_process.stderr.on('data', function(data){ 
  console.log(data.toString());
});