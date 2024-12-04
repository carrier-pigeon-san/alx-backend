const { createClient } = require("redis");
const kue = require("kue");
const express = require("express");

const queue = kue.createQueue();
const client = createClient({
  host: "localhost",
  port: 6379,
});

let reservationEnabled = true;

client.on("connect", () => {
  client.set(`available_seats`, 50);
});

function reserveSeat(number) {
  client.set(`available_seats`, number);
}

function getCurrentAvailableSeats() {
  return new Promise((resolve, reject) => {
    client.get(`available_seats`, (err, reply) => {
      if (err) {
        reject(err);
      }
      resolve(reply);
    });
  });
}

const app = express();
const port = 1245;

app.get("/available_seats", async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get("/reserve_seat", async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: "Reservation are blocked" });
    return;
  }

  const job = queue.create("reserve_seat", {}).save((err) => {
    if (!err) {
      res.json({ status: "Reservation in process" });
    } else {
      res.json({ status: "Reservation failed" });
    }
  });

  job.on("complete", () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on("failed", (error) => {
    console.log(`Seat reservation job ${job.id} failed: ${error}`);
  });
});

app.get("/process", async (req, res) => {
  const job = queue.process("reserve_seat", async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    if (availableSeats === "0") {
      done(new Error("Not enough seats available"));
    } else {
      reserveSeat(availableSeats - 1);
    }
    if (availableSeats - 1 === 0) {
      reservationEnabled = false;
    }
    done();
  });

  res.json({ status: "Queue processing" });
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});
