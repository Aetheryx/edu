/**
 * Een simpele functie om alle posts te vinden.
 * Dit wordt b.v. gebruikt voor de index pagina.
 */

module.exports = async function getAll ({ posts }) {
  return posts.find({}).toArray();
};
