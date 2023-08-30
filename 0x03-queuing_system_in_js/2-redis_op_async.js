import * as redis from 'redis';
import { promisify } from 'util';

const { createClient } = redis;
const client = createClient();

client.on('ready', () => console.log('Redis client connected to the server'));

client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
  const { get } = client;
  const getPromisified = promisify(get).bind(client);

  ((async () => {
    console.log(await getPromisified(schoolName));
  })());
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
