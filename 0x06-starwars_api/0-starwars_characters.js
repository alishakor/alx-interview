#!/usr/bin/node

// Write a script that prints all characters of a Star Wars movie:

// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line
// You must use the Star wars API
// You must use the module request

const reqst = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films';

reqst.get(`${url}/${movieId}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const reqst = JSON.parse(body);
    const charname = reqst.characters;
    for (let i = 0; i < charname.length; i++) {
      const ohk = charname[i];
      req.get(`${ohk}`, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const newres = JSON.parse(body);
          console.log(newres.name);
        }
      });
    }
  }
});
