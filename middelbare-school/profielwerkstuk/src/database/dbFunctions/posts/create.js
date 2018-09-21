/**
 * Een simpele functie voor het aanmaken van een post.
 */

module.exports = async function create ({ posts }, options) {
  // We voegen ook een aanmaaktijdstip toe.
  options.createdAt = Date.now();

  return posts.insertOne(options);
};
