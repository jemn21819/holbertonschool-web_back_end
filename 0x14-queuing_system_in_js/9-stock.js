const kue = require('kue')
const queue = kue.createQueue();
const express = require('express')
const app = express()
const port = 1245
const redis = require("redis");
const client = redis.createClient();
const { promisify } = require('util');
const getAsync = promisify(client.get).bind(client);
const listProducts = [
    {
      'Id': 1,
      'name': 'Suitcase 250',
      'price': 50,
      'stock': 4
    },
    {
      'Id': 2,
      'name': 'Suitcase 450',
      'price': 100,
      'stock': 10
    },
    {
      'Id': 3,
      'name': 'Suitcase 650',
      'price': 350,
      'stock': 2
    },
    {
      'Id': 4,
      'name': 'Suitcase 1050',
      'price': 550,
      'stock': 5
    }
  ]

  function getItemById(id) {
    return (listProducts.find(x => x.Id === id));
  }

  app.listen(port, () => {
    console.log(`Eserver listening on port:${port}`)
  })

  app.get('/list_products', (request, response) => {
    return response.json(listProducts)
})

function reserveStockById (itemId, stock){
    const item = getItemById(itemId);
    client.set(item.stock, stock);
    getItemById(itemId);
}
async function getCurrentReservedStockById(itemId) {
    const item =  getItemById(itemId);
    return (await getAsync(item.stock));
  }
  app.get('/list_products/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);
  
    if (!item) {
      res.json({ status: 'Product not found' });
      return;
    }
  
    const currentStock = await getCurrentReservedStockById(itemId);
    const stock =
      currentStock === null ? item.initialAvailableQuantity : currentStock;
  
    item.currentQuantity = stock;
    res.json(item);
  });
  
  
  app.get('/reserve_product/:itemId', (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);
    if (item == undefined )
      return (res.json({status: 'Product not found'}));
    console.log('STOCK ', item.stock);
    if (item.stock < 1)
      return (res.json({status:'Not enough stock available', itemId: itemId}));
  
    reserveStockById(itemId, 1);
    res.json({status:'Reservation confirmed', itemId: itemId});
  })