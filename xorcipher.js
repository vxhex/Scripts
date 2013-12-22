/*
 * XOR Cipher for shits-n-giggles
 * Usage: var ciphertext = xorcipher('stuff', 41);
 */
function xorcipher(str, xor) {
  var cry = "";
  for (var i = 0; i < str.length; i++) {
    cry += String.fromCharCode(str.charCodeAt(i) ^ xor);
  }
  return cry;
}

