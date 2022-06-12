const http = require('http');
const data = require('./3-read_file_async');

const app = http.createServer();
app.on('request', (request, response) => {
  if (request.method === 'GET' && request.url === '/students') {
    data(process.argv[2]).then((r) => {
      response.end(`This is the list of our students\n${r}`);
    }).catch((e) => {
      response.write('This is the list of our students\n');
      response.end(e.message);
    });
  } else {
    const body = 'Hello Holberton School!';
    response.end(body);
  }
});
app.listen(1245);
module.exports = app;
