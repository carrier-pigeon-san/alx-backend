import { createClient, print } from "redis";

const client = createClient({
  host: "localhost",
  port: 6379,
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

process.on('SIGINT', () => {
  client.quit();
});

client.hset('HolbertonSchools', 'Portland', '50', (err, reply) => {
  print(`Reply: ${reply}`);
});

client.hset('HolbertonSchools', 'Seattle', '80', (err, reply) => {
  print(`Reply: ${reply}`);
});

client.hset('HolbertonSchools', 'New York', '20', (err, reply) => {
  print(`Reply: ${reply}`);
})

client.hset('HolbertonSchools', 'Bogota', '20', (err, reply) => {
  print(`Reply: ${reply}`);
})

client.hset('HolbertonSchools', 'Cali', '40', (err, reply) => {
  print(`Reply: ${reply}`);
})

client.hset('HolbertonSchools', 'Paris', '2', (err, reply) => {
  print(`Reply: ${reply}`);
})

client.hgetall('HolbertonSchools', (err, reply) => {
  console.log(reply);
})
