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

export default client;
