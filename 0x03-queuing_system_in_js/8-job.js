const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  
  for (const j of jobs) {
    const job = queue.create('push_notification_code_3', j);
    job.on('complete', (job) => console.log(`Notification job ${job.id} completed`))
       .on('failed', (error) => console.log(`Notification job ${job.id} failed ${error}`))
       .on('progress', (progress, data) => console.log(`Notification job ${job.id} ${progress}% complete`));
   job.save(error => {
      if (!error) {
        console.log(`Notification job created: ${job.id}`);
      }
   });
  }
};

export default createPushNotificationsJobs;
