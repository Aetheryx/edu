/**
 * Dit is het start bestand.
 * Dit is dus het bestand wat je "opstart" met Node.js.
 * In dit bestand importeren we het kernbestand en "config.json",
 * een bestand met onze sessie-encryptie-sleutel
 * en de poort waarop de website moet draaien.
 */

const config = require(`${__dirname}/config.json`);
const main = require(`${__dirname}/src/main.js`);

main(config);
