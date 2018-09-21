/**
 * Een simpele functie voor het maken van een comment op een post.
 */

module.exports = async function create ({ comments }, options) {
  options.createdAt = Date.now();

  return comments.insertOne(options);
};
