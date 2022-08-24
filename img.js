// const getPixels = require('get-pixels');
// const src = `image.png`;

// getPixels(src, function(err, pixels) {
//   if(err) {
//     console.log("Bad image path");
//     return;
//   }

//   for (let y = 0; y < pixels.shape[1]; y++) {
//     for (let x = 0; x < pixels.shape[0]; x++) {

//       const r = pixels.get(x, y, 0);
//       const g = pixels.get(x, y, 1);
//       const b = pixels.get(x, y, 2);
//       const a = pixels.get(x, y, 3);
//       const rgba = `color: rgba(${r}, ${g}, ${b}, ${a});`;
//       console.log(rgba);
//     }
//   }
// });


const getPixels = require("get-pixels")

getPixels("image.png", function(err, pixels) {
  if(err) {
    console.log("Bad image path")
    return
  }
  console.log("got pixels", pixels.shape.slice())
})