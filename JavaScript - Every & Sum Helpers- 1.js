var names = [
	"Alexandria",
  "Mathew",
  "joe"
];

// Not every name is greater than 4 characters

names.every(function(name) {
  return name.length > 4;
});

// At least some of the names are greater than 4 characters

names.some(function(name) {
	return name.length > 4;
});
