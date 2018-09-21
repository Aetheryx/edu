/**
 * Een simpele functie voor het maken van vinden van alle comments op een post.
 */

module.exports = async function get ({ comments }, _id) {
  return comments.find({ parentPost: _id }).toArray();
};
