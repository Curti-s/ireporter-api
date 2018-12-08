[![Build Status](https://travis-ci.org/Curti-s/ireporter-api.svg?branch=develop)](https://travis-ci.org/Curti-s/ireporter-api) [![Coverage Status](https://coveralls.io/repos/github/Curti-s/ireporter-api/badge.svg?branch=develop)](https://coveralls.io/github/Curti-s/ireorter-api?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/1096ea8fa9ab65d34be4/maintainability)](https://codeclimate.com/github/Curti-s/ireporter-api/maintainability)  [ ![Codeship Status for Curti-s/iReporter](https://app.codeship.com/projects/ffbb4340-d7b8-0136-f968-1a3619919e04/status?branch=develop)](https://app.codeship.com/projects/317154) [![BCH compliance](https://bettercodehub.com/edge/badge/Curti-s/ireporter-api?branch=develop)](https://bettercodehub.com/)

# ireporter-api

It is a corruption reporting platform that enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.


## Getting Started

Clone the project

`git clone https://github.com/Curti-s/ireporter-api.git`


### Prerequisites

You require a python virtual environment. Use venv module provided by python

`python -m venv venv`

### Installing

Source the .env file that contains the project's settings and automatically creates a 
virtual environment
`source .env`

Install the project dependecies using the requirements file

`pip install -r requirements.txt`

Run the flask application

`flask run`


## Running the endpoints

Test the red-flag api endpoints using postman or curl. HTTP methods allowed `GET POST PUT DELETE`
`Use the following routes:
    
    localhost:5000/ **POST** create a new red-flag
    localhost:5000/ **GET** all red-flags
    localhost:5000/redflag/ **POST** create a red-flag
    localhost:5000/redflag/ **GET** get all red-flags
    localhost:5000/redflag/id **GET** a specific red-flag
    localhost:5000/redflag/id **PUT** update the location of a specific red-flag 
    localhost:5000/redflag/id **DELETE** delete a specific red-flag

`


### Breaking down the tests

Use pytest to run the tests

`pytest tests/`




## Deployment

Change the `FLASK_ENV` variable value to `production` 

`FLASK_ENV=production`

and source the environment

`source .env`

## Authors

* [**Matthew Kirimi**](https://github.com/Curti-s)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


