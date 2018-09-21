/**
 * Met deze functie kunnen we een bepaalde post vinden via de post ID.
 * Met MongoDB kunnen we de postID in de vorm van een string omzetten naar een Object, waar MongoDB mee kan zoeken.
 */

const { ObjectID } = require('mongodb');

module.exports = async function get ({ posts }, _id) {
  try {
    _id = ObjectID(_id);
  } catch (e) {
    _id = null;
  }

  return posts.findOne({ _id });
};
