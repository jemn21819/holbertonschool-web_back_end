const redis = require('redis');
const client = redis.createClient();

client.on('error', function(error) {
    console.error(`Redis client not connected to the server: ${error}`);
  });
  client.on('ready', function()  {
    console.log('Redis client connected to the server');
  });

  function publishMessage(message, time){
      setTimeout(() => {
          console.log(`About to send ${message}`)
          client.PUBLISH('holberton school Channel', message, (error) => {
        });

      }, time);

  }
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400)