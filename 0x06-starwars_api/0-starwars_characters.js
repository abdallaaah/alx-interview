#!/usr/bin/node

const { promises } = require('dns')
const request = require('request')
let x = process.argv[2]
url = `https://swapi-api.alx-tools.com/api/films/${x}`
request(url, (error, response, body) =>{
    if (error) {
        console.log(error)
    }
    body = JSON.parse(body)
    list_of_character = body['characters']
    Promise.all(list_of_character.map(url => request(url, (error, response2, body2)=>{
        x = JSON.parse(body2)
        console.log(x['name'])
    })))
    
})
