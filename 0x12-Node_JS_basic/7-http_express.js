const express = require('express');
const data = require('./3-read_file_async');

const app = express();
app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});
app.get('/students', (request, response) => {
  data(process.argv[2]).then(({ r }) => {
    response.send(`This is the list of our students\n${r.join('\n')}`);
  }).catch((e) => {
    response.send(`This is the list of our students\n${e.message}`);
  });
});
app.listen(1245);
module.exports = app;
