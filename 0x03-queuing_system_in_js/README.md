# Queuing System in JavaScript

This project focuses on implementing a queuing system using JavaScript. The goal is to understand the concepts of queues and how they can be applied in real-world scenarios.

## Table of Contents
- [Introduction](#introduction)
- [Objectives](#objectives)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Introduction
A queuing system is a data structure that follows the First In First Out (FIFO) principle. This project demonstrates how to create and manage a queue using JavaScript.

## Objectives
- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to the build a basic Express app interacting with a Redis server and queue

## Features
- Enqueue: Add an element to the end of the queue.
- Dequeue: Remove an element from the front of the queue.
- Peek: View the element at the front of the queue without removing it.
- Size: Get the number of elements in the queue.
- isEmpty: Check if the queue is empty.

## Installation
To get started with this project, clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/queuing_system_in_js.git
cd queuing_system_in_js
```

## Usage
To use the queuing system, include the `queue.js` file in your project and create an instance of the Queue class:
```javascript
const Queue = require('./queue');

const myQueue = new Queue();
myQueue.enqueue('Task 1');
myQueue.enqueue('Task 2');
console.log(myQueue.dequeue()); // Output: Task 1
```
