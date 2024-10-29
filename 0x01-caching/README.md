# Caching in Python

This project folder contains various implementations and exercises related to caching mechanisms in Python. The goal is to understand different caching strategies and how they can be applied to optimize performance in software applications.

## Table of Contents

- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Caching Strategies](#caching-strategies)
    - [Basic Caching](#basic-caching)
    - [LRU Cache](#lru-cache)
    - [LFU Cache](#lfu-cache)
- [Files](#files)

## Introduction

Caching is a technique used to store frequently accessed data in a temporary storage area, so that future requests for that data can be served faster. This project explores different caching strategies and their implementations in Python.

## Learning Objectives

- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

## Caching Strategies

### Basic Caching

Basic caching involves storing data in a simple key-value store. This is the simplest form of caching and is useful for small datasets.

### LRU Cache

LRU (Least Recently Used) cache evicts the least recently accessed items first. This is useful when you want to ensure that frequently accessed items remain in the cache.

### LFU Cache

LFU (Least Frequently Used) cache evicts the least frequently accessed items first. This is useful when you want to ensure that items accessed more frequently remain in the cache.

## Files

- **0-basic_cache.py**

- **1-fifo_cache.py**

- **2-lifo_cache.py**

- **3-lru_cache.py**

- **4-mru_cache.py**

- **100-lfu_cache.py**
