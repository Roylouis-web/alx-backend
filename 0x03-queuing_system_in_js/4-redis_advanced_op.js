import * as redis from 'redis';

const { createClient } = redis;

const client = createClient();

client.on('ready', () => console.log('Redis client connected to the server'));

client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

client.hset('HolbertonSchools', 'Portland', '50', redis.print);
client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
client.hset('HolbertonSchools', 'New York', '20', redis.print);
client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
client.hset('HolbertonSchools', 'Cali', '40', redis.print);
client.hset('HolbertonSchools', 'Paris', '2', redis.print);

client.hgetall('HolbertonSchools', (error, values) => console.log(values));
