const kue = require('kue');
const queue = kue.createQueue();
const blacked = [
     '4153518780',
     '4153518781'
]

queue.process('push_notification_code_2', function(job, done) {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
function sendNotification(phoneNumber, message, job, done){

    job.progress(0, 100);
    if (blacked.includes(phoneNumber)) {
	console.log(`Phone number ${phoneNumber} is blacklisted `);
    }
    job.progress(0, 50);
    console.log(`Sending notification to ${phoneNumber} with message: ${message}`);
    done();
}