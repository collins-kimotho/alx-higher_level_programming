#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the Star Wars API for the given movie ID
request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Check if the data contains a characters field
  if (body && Array.isArray(body.characters)) {
    // Fetch each character's details and print their names
    body.characters.forEach((characterUrl) => {
      request.get(characterUrl, { json: true }, (err, res, characterBody) => {
        if (err) {
          console.error('Error:', err);
          return;
        }

        // Print the character's name
        if (characterBody && characterBody.name) {
          console.log(characterBody.name);
        }
      });
    });
  } else {
    console.log('No characters found for this movie.');
  }
});
