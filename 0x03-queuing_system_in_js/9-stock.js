import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4
  },

  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10
  },

  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 100, 
    initialAvailableQuantity: 10
  },

  {
    itemId: 4,
    itemName: 'Suitcase 1050', 
    price: 550,
    initialAvailableQuantity: 5
  }
];

const app = express();
const client = createClient();

client.on('ready', () => console.log('Redis client connected to the server'));
client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

const getItemById = (id) => {
  const foundProduct = listProducts.find(product => product.itemId === id);
  return foundProduct;
};

const reserveStockById = (itemId, stock) => {
  client.set(itemId, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const { get } = client;
  const getPromisified = promisify(get).bind(client);
  return ((async () => await getPromisified(itemId))());
}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  let currentStock = await getCurrentReservedStockById(itemId);
  let currentQuantity;
  const product = getItemById(parseInt(itemId));
  
  if (!product) {
    return res.json({ status: "Product not found" });
  }

  if (!currentStock) {
    currentQuantity = product.initialAvailableQuantity
  } else {
    currentQuantity = product.initialAvailableQuantity - currentStock;
  }

  product.currentQuantity = product.initialAvailableQuantity - currentStock;
  res.json(product);
});

app.get('/reserve_product/:itemId', (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(parseInt(itemId));
  let response;

  if (!product) {
    response = { status: "Product not found" };
  } else if (product.initialAvailableQuantity < 1) {
    response = { status: "Not enough stock available", itemId };
  } else {
    reserveStockById(itemId, 1);
    response = { status: "Reservation confirmed", itemId };
  }
  
  res.json(response);
});

app.listen(1245);
