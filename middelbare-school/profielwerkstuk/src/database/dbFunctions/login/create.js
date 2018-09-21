/**
 * Met deze functie maken we een account aan.
 * We gebruiken hier de "bcrypt" module om het wachtwoord te hashen.
 * Door het wachtwoord te hashen staat het wachtwoord nooit in de database, maar alleen een "beschrijving" van het wachtwoord.
 * Dat is dus de hash zelf.
 * In database/dbFunctions/login/get.js zie je meer over hoe we dan een hash vergelijken met een wachtwoord.
 */

const { randomString } = require(`${__dirname}/../../../utils`);
const { hash } = require('bcrypt');

module.exports = async function create ({ login }, options) {
  // De functie die de hash aanmaakt.
  // 10 is hier de intensiteit - een hogere intensiteit is moeilijker te brute-forcen, maar zal ook meer kracht kosten om aan te maken.
  options.password = await hash(options.password, 10);
  options.token = randomString(32); // Het inlog-token. Dit is intern.
  options.createdAt = Date.now(); // We voegen ook een parameter toe voor wanneer het account aan is gemaakt.

  await login.insertOne(options);

  return options.token;
};
