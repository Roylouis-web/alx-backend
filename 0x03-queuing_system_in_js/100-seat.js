import { promisify } from 'util';
import { createClient } from 'redis';
import { createQueue } from 'kue';
import express from 'express';

const client = createClient();
const queue = createQueue();
const app = express();
let reservationEnabled = true;

const reserveSeat = (number) => {
  client.set('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const { get } = client;
  const getPromisified = promisify(get).bind(client);
  return await getPromisified('available_seats');
};

reserveSeat(50);

app.get('/available_seats', async (req, res) => {
  const available_seats = await getCurrentAvailableSeats();
  return res.json({ numberOfAvailableSeats : available_seats });
});

app.get('/reserve_seat', (req, res) => {
  let response;

  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  } else {
    const job = queue.create('reserve_seat', { seat: '1' }).save(error => {
      if (error) {
	return res.json({ status: 'Reservation failed' });
      } else {
	return res.json({ status: 'Reservation in process' });
	job.on('complete', (job) => console.log(`Seat reservation job ${job.id} completed`));
	job.on('failed', (error) => console.log(`Seat reservation job ${job.id} failed: ${error}`));
      }
    });
  }
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = parseInt(await getCurrentAvailableSeats());
    if (availableSeats === 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      const newNumber = availableSeats - 1;
      reserveSeat(newNumber);
      return res.json({ status: 'Queue processing' });
      done();
    }
  });
});

app.listen(1245);
