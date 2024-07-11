#!/usr/bin/node

const request = require('request');
let x = process.argv[2];
let url = `https://swapi-api.alx-tools.com/api/films/${x}`;

// Function to wrap request in a promise
function fetch(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                return reject(error);
            }
            resolve(JSON.parse(body));
        });
    });
}

request(url, (error, response, body) => {
    if (error) {
        console.log(error);
        return;
    }
    body = JSON.parse(body);
    let list_of_character = body['characters'];

    // Map each URL to its index and fetch the character data
    Promise.all(list_of_character.map((url, index) => 
        fetch(url).then(character => ({ index, character }))
    ))
    .then(results => {
        // Sort the results based on the original order
        results.sort((a, b) => a.index - b.index);
        results.forEach(result => {
            console.log(result.character.name);
        });
    })
    .catch(error => {
        console.log(error);
    });
});
