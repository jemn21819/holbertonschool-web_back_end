const redis = require('redis');
const client = redis.createClient();

client.on('error', function(error) {
    console.error(`Redis client not connected to the server: ${error}`);
  });
  client.on('ready', function()  {
    console.log('Redis client connected to the server');
  });

  client.SUBSCRIBE('holberton school Channel', function (error){
  });
  client.on('message',  function(Channel , message){
    if (Channel === 'holberton school Channel') {
        console.log(message);
    }
    if (message === 'KILL_SERVER') {
        client.UNSUBSCRIBE(message, function(error){
        });
        client.quit();
    }
  });
  