import kue from 'kue';

import createPushNotificationsJobs from './8-job';

import { describe, it, before, after, afterEach } from 'mocha';

import assert from 'assert';

const { createQueue } = kue;
const queue = createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });
  
  after(() => {
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array', () => {
    assert.throws(() => createPushNotificationsJobs('name', queue), { message: 'Jobs is not an array' });
  });
  
  it('create two new jobs to the queue', () => {
    const list = [
      {
        phoneNumber: '4153518780',
	message: 'This is the code 1234 to verify your account'
      }
    ];
    createPushNotificationsJobs(list, queue);
    assert(queue.testMode.jobs[0].type, 'push_notification_code_3');
    assert(queue.testMode.jobs[0].data, list);
  });
});

