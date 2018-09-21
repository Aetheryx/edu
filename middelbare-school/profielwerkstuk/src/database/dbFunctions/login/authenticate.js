/**
 * Met deze functie kunnen gebruikers een token omwisselen voor een gebruikersnaam, en dus een sessie.
 * Dit is dus de functie die opgeroepen wordt wanneer gebruikers willen inloggen.
 */

module.exports = async function authenticate ({ login }, token) {
  return login.findOne({ token });
};
