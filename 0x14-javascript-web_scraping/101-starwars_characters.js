#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode == 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    let count = 0;

    const printCharacter = () => {
      if (count < characters.length) {
        request(characters[count], function (error, response, body) {
          if (!error && response.statusCode == 200) {
            const character = JSON.parse(body);
            console.log(character.name);
            count++;
            printCharacter();
          }
        });
      }
    };

    printCharacter();
  }
});
