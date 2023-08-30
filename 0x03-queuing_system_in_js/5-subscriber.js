import * as redis from 'redis';

const { createClient } = redis;

const subscriber = createClient();

subscriber.on('ready', () => console.log('Redis client connected to the server'));

subscriber.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
  console.log(message);

  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe('holberton school channel');
    process.exit();
  }
});
