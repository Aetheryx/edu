/**
 * Hier vind je alle database functies.
 * In dit index.js bestand importeren we alle database functies naar een groot object, met de volgende structuur:
 * 
 * [Secties (b.v. posts, login)]
 *   [Sectie 1]
 *     [Functie 1 van sectie 1]
 *     [Functie 2 van sectie 1]
 *     [Functie 3 van sectie 1]
 *   [Sectie 2]
 *     [Functie 1 van sectie 2]
 *     [Functie 2 van sectie 2]
 *     [Functie 3 van sectie 2]
 *   [Sectie 3]
 *     [Functie 1 van sectie 3]
 *     [Functie 2 van sectie 3]
 *     [Functie 3 van sectie 3]
 *
 * Hierdoor kunnen we dus een bepaalde functie aanpakken, bijvoorbeeld Secties.Sectie1.Functie1.
 */

const { MongoClient } = require('mongodb');
const { readdirSync } = require('fs');

const config = require(`${__dirname}/../../config.json`);
const { log } = require(`${__dirname}/../utils`);

async function createDB () {
  // Hier maken we de initiele verbinding met MongoDB.
  const dbClient = await MongoClient.connect(config.dbURL || 'mongodb://localhost:27017')
    .catch(e => {
      // Als dit fout gaat, kan het programma helemaal niet werken. Daarom sluiten we het programma af.
      log('Verbinding met MongoDB mislukt. Process sluit af...');
      process.exit(1);
    });

  const dbConn = dbClient.db('PWS');

  const tables = {
    login: dbConn.collection('login'),
    posts: dbConn.collection('posts'),
    comments: dbConn.collection('comments')
  };

  const dbFunctions = {};

  const databaseTables = readdirSync(`${__dirname}/dbFunctions`);

  for (const databaseTable of databaseTables) {
    dbFunctions[databaseTable] = {};
    const tableFunctions = readdirSync(`${__dirname}/dbFunctions/${databaseTable}`);
    for (const tableFunction of tableFunctions) {
      dbFunctions
        [databaseTable]
        [tableFunction.split('.').shift()] =
          require(`${__dirname}/dbFunctions/${databaseTable}/${tableFunction}`)
            .bind(null, tables);
    }
  }

  return {
    dbFunctions,
    dbConn
  };
}

module.exports = createDB();
