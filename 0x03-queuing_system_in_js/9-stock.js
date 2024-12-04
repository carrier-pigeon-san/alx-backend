const express = require('express');
const redis = require('redis');

const client = redis.createClient({
  host: 'localhost',
  port: 6379
});
const app = express();
const port = 1245;

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  }
];

function getItemById(id) {
  return listProducts.find(product => product.id === id);
}

function reserveStock(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

function getCurrentReservedStockById(itemId) {
  return new Promise((resolve, reject) => {
    client.get(`item.${itemId}`, (err, reply) => {
      if (err) {
        reject(err);
      }
      resolve(reply);
    });
  });
}

app.get('/list_products', (req, res) => {
  const result = listProducts.map(product => {
    return {
      "itemId": product.id,
      "itemName": product.name,
      "price": product.price,
      "initialAvailableQuantity": product.stock
    };
  });
  res.json(result);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.status(404).json({ "status": "Product not found" });
    return;
  }
  const reservedStock = await getCurrentReservedStockById(itemId);
  const result = {
    "itemId": item.id,
    "itemName": item.name,
    "price": item.price,
    "initialAvailableQuantity": item.stock,
    "currentQuantity": reservedStock
  };
  res.json(result);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.status(404).json({ "status": "Product not found" });
    return;
  }
//   const reservedStock = await getCurrentReservedStockById(itemId);
//   if (reservedStock === '0' || !reservedStock) {
  if (item.stock === 0) {
    res.status(403).json({ "status": "Not enough stock available", "itemId": itemId });
    return;
  }
  reserveStock(itemId, 1);
  res.json({ "status": "Reservation confirmed", "itemId": itemId });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
