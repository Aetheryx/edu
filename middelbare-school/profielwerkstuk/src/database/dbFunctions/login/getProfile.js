/**
 * Met deze functie kan je een bepaald profiel opvangen van een gebruiker.
 */

module.exports = async function getProfile ({ login }, username) {
  return login.findOne({
    // We gebruiken hier een regex met de "i" flag zodat het niet hoofdlettergevoelig is.
    username: new RegExp(username, 'i')
  });
};
