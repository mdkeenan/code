// Create function that filters out all numbers > than 15

var numbers = [10, 12, 13, 20, 30];
function reject(array, iteratorFunction) {
  return array.filter(arr => !iteratorFunction(arr));
}

function iteratorFunction(array){
   return array > 15;
}

var lessThanFifteen = reject(numbers, iteratorFunction);
