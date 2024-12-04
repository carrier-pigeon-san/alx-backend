const kue = require('kue');

const push_notification_code = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, you have a new notification',
};

const job = push_notification_code.create('push_notification_code', jobData).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

job.on('progress', (progress) => {
  console.log(`Notification job ${job.id} ${progress}% complete`);
});
