#!/usr/bin/node

// Write a script that prints all characters of a Star Wars movie:

// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line
// You must use the Star wars API
// You must use the module request

const request = require('request');
const movieId = process.argv[2];
const ApiUrl = 'https://swapi-api.alx-tools.com/api';

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Request failed with status code ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function fetchMovieAndCharacters (movieId) {
  try {
    const movieData = await getRequest(`${ApiUrl}/films/${movieId}`);
    const characterPromises = movieData.characters.map(characterUrl =>
      getRequest(characterUrl).then(characterData => characterData.name)
    );

    const characterNames = await Promise.all(characterPromises);
    characterNames.forEach(characterName => {
      console.log(`${characterName}`);
    });
  } catch (error) {
    console.error(`Error: ${error}`);
  }
}

fetchMovieAndCharacters(movieId);
