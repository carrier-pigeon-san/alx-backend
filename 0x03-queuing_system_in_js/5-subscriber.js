import { createClient } from "redis";

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

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  console.log(message);

  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  }
});
