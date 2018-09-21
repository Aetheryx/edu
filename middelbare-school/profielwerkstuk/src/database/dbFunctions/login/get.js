/**
 * De get functie. Hiermee wordt gekeken of een gebruikersnaam+wachtwoord correct is.
 * We gebruiken bcrypt om de opgeslagen hash te vergelijken met het wachtwoord.
 */

const { compare } = require('bcrypt');

module.exports = async function get ({ login }, username, password) {
  // We pakken eerst het account.
  const account = await login.findOne({ username });

  // Als de hash van het account overeenkomt met het wachtwoord, geven we het door.
  if (await compare(password, account ? account.password : '')) {
    return account;
  }
};
