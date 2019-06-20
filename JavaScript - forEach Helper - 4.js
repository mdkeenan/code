 var images = [
  { height: 10, width: 30 },
  { height: 20, width: 90 },
  { height: 54, width: 32 }
];
 
var areas = [];
 
  function imager(image){
   areas.push(image.height*image.width);
 }
 
 images.forEach(imager);

areas

// Output
// [300,1800,1728]
