const redis = require("redis");
const client = redis.createClient();

client.on('error', function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});
client.on('ready', function()  {
  console.log('Redis client connected to the server');
});