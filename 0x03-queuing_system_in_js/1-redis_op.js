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

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
    print(`Reply: ${reply}`);
  });
}

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
