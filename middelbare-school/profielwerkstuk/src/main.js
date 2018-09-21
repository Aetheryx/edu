/**
 * Dit is "where the magic happens"!
 * In dit bestand importeren we alle belangrijke functies en bibliotheken.
 * We plakken ze dan samen tot een geheel.
 */

const express = require('express'); // "require" importeert een bibliotheek, of een local bestand. Hier importeren we express.

const bodyParser = require('body-parser');

// Het verbinden van onze express-sessie met MongoDB.
const session = require('express-session');
const MongoDBStore = require('connect-mongo')(session); 

const { router } = require(`${__dirname}/web`);
const { log } = require(`${__dirname}/utils`);

module.exports = async function init (config) {
  const app = express();
  // Hier importeren we de database functies. Met deze functies kunnen we dingen plaatsen of krijgen vanuit de database.
  const { dbFunctions, dbConn } = await require(`${__dirname}/database`);

  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: false }));
  app.use('/css', express.static(`${__dirname}/web/views/css`));

  app.use(session({
    secret: config.secret,
    resave: true,
    saveUninitialized: false,
    store: new MongoDBStore({ // We geven onze mongodb-session-opslag door aan Express.
      dbPromise: Promise.resolve(dbConn)
    })
  }));

  // In deze twee regels verbinden we het frontend met het backend.
  // Nu kunnen we vanuit het backend (Express) frontend renderen (in EJS/HTML en CSS).
  app.set('views', `${__dirname}/web/views`);
  app.set('view engine', 'ejs');

  for (const route in router) {
    router[route](app, dbFunctions); // Elke route (pagina) in de router initiëren.
  }

  // Deze functie start de webserver op. Nu luistert Express op een bepaalde poort naar verzoeken.
  app.listen(config.port, () => { 
    log(`Listening on ${config.port}`);
  });
};
