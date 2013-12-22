/*
 * Triangle coding exercise
 * Usage: console.log(triangle(5));
 */
function triangle(rows) {
  var output = '';
  for(var z = 1; z <= rows; z++) {
    for(var x = 0; x < rows-z; x++) {output += ' ';}
    for(var y = 0; y < z+(z-1); y++) {output += 'x';}
    output += '\n';
  }
  return output;
}
