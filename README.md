[![Build Status](https://travis-ci.org/steveviko/SendIT.svg?branch=challenge3)](https://travis-ci.org/steveviko/SendIT)
[![Coverage Status](https://coveralls.io/repos/github/steveviko/SendIT/badge.svg?branch=challenge2)](https://coveralls.io/github/steveviko/SendIT?branch=challenge2)
[![Maintainability](https://api.codeclimate.com/v1/badges/2b9eb6fa3784abf79d79/maintainability)](https://codeclimate.com/github/steveviko/SendIT/maintainability)
# SendIT

- SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes    based on weight categories.

## Getting Started
- These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


## Requirements
- For development, you will only need flask installed on your environement
**Clone this _Repository_**
  
$ https://github.com/steveviko/SendIT/tree/develop  to your computer
$ cd SendIT
 
 ###  Installation Steps
  
    1.Make a Virtual Environment
    2.Connect our project with our Environment
    3.Set Project Directory
    4.Activate virtual enviroment by typing ```Workon```
    5.Pip Install Flask!
 

 ## Tools

- ` Python3.6 `- A High Level Programming Language
- `Flask `- Python based web framework
- `Pytest` - A Python testing framework which makes it easy to write small tests, yet scales to support complex         functional    testing for applications and libraries
- `Virtualenv` - A tool to create isolated virtual environment
- ` Postgresql` - PostgreSQL is a powerful, open source object-relational database system.
 
### Running the tests
To run tests execute this command below in your terminal
```
$ nosetests example_unit_test.py
```
**Create virtual environment and install it**
```
$ virtualenv - -python = python3 venv
$ source / venv/bin/activate
```
**Install all the necessary _dependencies_ by**
```
$ pip install - r requirements.txt
```
**Run _app_ by**
```
$ python run.py
$ At the terminal or console execute the run.py file
```
## Project APIs
|           End Point | Functionality |
| -------------------------------------- | ----------------------------------------- |
|     POST   api/v2/parcels/auth/signup      | Create a parcel delivery order |
| POST   api/v2/parcels /auth/login     | Create a parcel delivery order |
| POST   api/v2/parcels      | Create a parcel delivery order |
|PUT  api/v2/parcels/<parcelId>/destination|Change the location of a specific parcel delivery order |
|PUT  api/v2/parcels/<parcelId>/presentLocation|Change the present location of a specific parcel delivery order |
|PUT  api/v2/parcels/<parcelId>/status|Change the status of a specific parcel delivery order |
| GET api/v2/parcels/<parcelId> | Fetch a specific parcel delivery order|
| GET api/v2/users/<userId>/parcels | Fetch all parcel delivery orders by a specific user |
|     GET  api/v2/parcels  | Fetch all parcel delivery orders |

Open the browser to view the endpoints with their specifications
```
localhost:5000 
```

## Contributors
- [Steven Opio](https://github.com/steveviko)

## This Platform is served by  
- Git-pages [GitHub Pages](https://steveviko.github.io/SendIT/UI/index.html). 

## Demo
- The API is hosted [Here](https://venvikosendit.herokuapp.com/api/v1/parcels)

## MIT License

Copyright (c) 2018 **VenViko**
