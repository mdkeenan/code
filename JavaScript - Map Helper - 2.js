var cars = [
	{ model: 'Buick', price: 'CHEAP' },
  { model: 'Camaro', price: 'expensive' }
];

// Example of 'plucking' a property from an array
var prices = cars.map(function(car) {
  return car.price;
});

prices;
