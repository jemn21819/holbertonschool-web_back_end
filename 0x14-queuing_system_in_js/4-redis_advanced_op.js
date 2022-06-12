const redis = require('redis');
const client = redis.createClient();

client.on('error', function(error) {
    console.error(`Redis client not connected to the server: ${error}`);
  });
  client.on('ready', function()  {
    console.log('Redis client connected to the server');
  });

client.hset('HolbertonSchools', 'Portland', '50', redis.print);
client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
client.hset('HolbertonSchools', 'New York', '20', redis.print);
client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
client.hset('HolbertonSchools', 'Cali', '40', redis.print);
client.hset('HolbertonSchools', 'Paris', '2', redis.print);

client.hgetall('HolbertonSchools', (error, val) => {
  console.log(val);
});