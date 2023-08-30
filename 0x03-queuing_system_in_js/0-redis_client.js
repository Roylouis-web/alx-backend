import * as redis from 'redis';

const { createClient } = redis;

const client = createClient();

client.on('ready', () => console.log('Redis client connected to the server'));

client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));
