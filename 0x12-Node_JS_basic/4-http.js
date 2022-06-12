const http = require('http');

const app = http.createServer();
app.on('request', (request, response) => {
  const body = 'Hello Holberton School!';
  response.end(body);
});
app.listen(1245);
module.exports = app;
