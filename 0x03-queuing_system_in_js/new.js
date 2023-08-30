import * as kue from 'kue';

const { createQueue } = kue;
const queue = createQueue();

queue
  .on('job complete', (id) => {
    kue.Jobs.get(id, (err, job) => job.remove());
  })
  .on('failed', () => console.log('Notification job failed'));
