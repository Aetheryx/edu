/**
 * Met deze functie wordt er gekeken of een bepaalde gebruikersnaam al in gebruik is.
 */

module.exports = async function isUsernameTaken ({ login }, username) {
  return login.findOne({ username })
    .then(Boolean); // We zetten het resultaat om in een Boolean, omdat er verder niets nodig is. Of de gebruikersnaam is beschikbaar, of niet.
};
