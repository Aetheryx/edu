/**
 * Met dit bestand krijgen we een string van willekeurige karakters, output in base64.
 * Dit is wat wordt gebruikt voor login tokens en andere cryptografische data.
 */

const { randomBytes } = require('crypto');

module.exports = function randomString (byteLength) {
  return randomBytes(byteLength).toString('base64');
};
