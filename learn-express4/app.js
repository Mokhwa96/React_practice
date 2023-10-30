const express = require('express');
const app = express();
const spawn = require('child_process').spawn;
const fs = require('fs').promises;
app.set('port', process.env.PORT || 3000);
app.get('/', (req, res) => {
  res.sendFile(__dirname, './public/index.html');
  app.use(express.static(__dirname + "/public")); // 외부 스크립트 이용
});
app.get('/python', (req, res) => { // localhost:3000/python 으로 접근할 때 사용하는 라우터
  const py_process = spawn('python', ['./public/py/crawl.py']) // 이곳으로 접근하면 파이썬 파일을 python 명령어로 실행한다
  py_process.stdout.on('data', function(data){
    console.log(data.toString()); // 실행된 결과를 표준출력인 명령 프롬프트에 전달하여 출력
});
  py_process.stderr.on('data', function(data){ // 실행이 안 되었을 때의 메시지
    console.log(data.toString());
  });
});
app.listen(app.get('port'), () => {
  console.log(app.get('port'), '번 포트에서 대기 중');
})