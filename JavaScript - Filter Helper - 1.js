var products = [
  { name: 'cucumber', type: 'vegetable' },
  { name: 'banana', type: 'fruit' },
  { name: 'celery', type: 'vegetable' },
  { name: 'orange', type: 'fruit' }
];
var filteredProducts = [];

// Old way using for loop
for (var i = 0; i < products.length; i++) {
	if (products[i].type === 'vegetable') {
    filteredProducts.push(products[i]);
  }                      
}

filteredProducts;

//new way using 

products.filter(function(product) {
	return product.type === 'fruit';
});
