 [![Build Status](https://travis-ci.org/Curti-s/iReporter.svg?branch=ch-heroku-%23162341804)](https://travis-ci.org/Curti-s/iReporter) [![Coverage Status](https://coveralls.io/repos/github/Curti-s/iReporter/badge.svg?branch=ch-heroku-%23162341804)](https://coveralls.io/github/Curti-s/iReporter?branch=ch-heroku-%23162341804) [![Maintainability](https://api.codeclimate.com/v1/badges/489c9a7588aba5098c2c/maintainability)](https://codeclimate.com/github/Curti-s/iReporter/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/489c9a7588aba5098c2c/test_coverage)](https://codeclimate.com/github/Curti-s/iReporter/test_coverage) [ ![Codeship Status for Curti-s/iReporter](https://app.codeship.com/projects/ffbb4340-d7b8-0136-f968-1a3619919e04/status?branch=ch-heroku-%23162341804)](https://app.codeship.com/projects/317154) [![BCH compliance](https://bettercodehub.com/edge/badge/Curti-s/iReporter?branch=develop)](https://bettercodehub.com/)

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


`
#### Examples

Creating a new red-flag 

**POST**

    localhost:5000
    localhost:5000/redflag

    Red flag attributes to test with postman or curl
    {

        "created_by" : "curtis",
        "record_type" : "red flag",
        "location" : "0.0236° S, 37.9062° E",
        "status" : "draft",
        "image" :  " ",
        "video" : " ",
        "comment" : "Red flag comment"
    }

**Reponnse**
    {
        "message": "Created red-flag record",
        "status": 201
    }

Get all red-flags

**GET**
    
    localhost:5000
    localhost:5000/redflag

**Response**

    {
        "data": [
            [
                {
                    "comment": "Red flag comment",
                    "created_by": "curtis",
                    "created_on": "Wed, 05 Dec 2018 18:01:04 GMT",
                    "id": "98fea86b-0725-4096-a5ae-a84f45fed634",
                    "image": " ",
                    "location": "0.0236° S, 37.9062° E",
                    "record_type": "red flag",
                    "status": "draft",
                    "video": " "
                },
                {
                    "comment": "Red flag comment",
                    "created_by": "curtis",
                    "created_on": "Wed, 05 Dec 2018 18:01:13 GMT",
                    "id": "531ced43-2744-4b31-8d29-982222d199ce",
                    "image": " ",
                    "location": "0.0236° S, 37.9062° E",
                    "record_type": "red flag",
                    "status": "draft",
                    "video": " "
                },
                {
                    "comment": "Red flag comment",
                    "created_by": "curtis",
                    "created_on": "Wed, 05 Dec 2018 18:01:14 GMT",
                    "id": "4dcefb6f-5aa9-48db-9113-6bac7487dd6b",
                    "image": " ",
                    "location": "0.0236° S, 37.9062° E",
                    "record_type": "red flag",
                    "status": "draft",
                    "video": " "
                },
                {
                    "comment": "Red flag comment",
                    "created_by": "curtis",
                    "created_on": "Wed, 05 Dec 2018 18:01:15 GMT",
                    "id": "68be857b-465b-49f7-b44a-d32004adc7ec",
                    "image": " ",
                    "location": "0.0236° S, 37.9062° E",
                    "record_type": "red flag",
                    "status": "draft",
                    "video": " "
                },
                {
                    "comment": "Red flag comment",
                    "created_by": "curtis",
                    "created_on": "Wed, 05 Dec 2018 18:01:15 GMT",
                    "id": "52aaf95c-f68c-4f7b-9e00-604da4aeacd6",
                    "image": " ",
                    "location": "0.0236° S, 37.9062° E",
                    "record_type": "red flag",
                    "status": "draft",
                    "video": " "
                },
                {
                    "comment": "Red flag comment",
                    "created_by": "curtis",
                    "created_on": "Wed, 05 Dec 2018 18:01:16 GMT",
                    "id": "1ec22146-f681-4058-960f-bf996cc8a552",
                    "image": " ",
                    "location": "0.0236° S, 37.9062° E",
                    "record_type": "red flag",
                    "status": "draft",
                    "video": " "
                }
            ]
        ],
        "status": 200
    }

Get a particular red-flag

**GET**
    
    localhost:5000/redflag/id

**Response**

    {
        "data": {
            "comment": "Red flag comment",
            "created_by": "curtis",
            "created_on": "Wed, 05 Dec 2018 16:50:31 GMT",
            "id": "779d8081-4cd3-4834-b4f6-41cb3edd60e9",
            "image": " ",
            "location": "0.0236° N, 37.9062° W",
            "record_type": "red flag",
            "status": "draft",
            "video": " "
        },
        "status": 200
    }

`


## Deployment

Change the `FLASK_ENV` variable value to `production` 

`FLASK_ENV=production`

and source the environment

`source .env`

## Authors

* [**Matthew Kirimi**](https://github.com/Curti-s)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


