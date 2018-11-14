[![Build Status](https://travis-ci.org/steveviko/SendIT.svg?branch=develop)](https://travis-ci.org/steveviko/SendIT)
[![Coverage Status](https://coveralls.io/repos/github/steveviko/SendIT/badge.svg?branch=challenge2)](https://coveralls.io/github/steveviko/SendIT?branch=challenge2)
[![Maintainability](https://api.codeclimate.com/v1/badges/2b9eb6fa3784abf79d79/maintainability)](https://codeclimate.com/github/steveviko/SendIT/maintainability)
# SendIT

- SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes    based on weight categories.

## Getting Started
- These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Installation
**Clone this _Repository_**

 - [clone](https://github.com/steveviko/SendIT/tree/develop) to your computer


 ## Tools
 ``` 
●	Server-Side Framework: <Flask Python Framework>
●	Linting Library: <Pylint, a Python Linting Library>
●	Style Guide: <PEP8 Style Guide>
●	Testing Framework: <unittest, test runner package>
 ```
### Running the tests
To run tests run this command below in your terminal

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
$ Python run.py
$ Run the server At the terminal or console type
```
## Project APIs
|           End Point | Functionality |
| -------------------------------------- | ----------------------------------------- |
|     POST   api/v1/parcels      | Create a parcel delivery order |
|PUT/parcels/<parcelId>/cancel|Cancel the specific parcel delivery order |
| GET /parcels/<parcelId> | Fetch a specific parcel delivery order|
| GET /users/<userId>/parcels | Fetch all parcel delivery orders by a specific user |
|     GET  api/v1/parcels  | Fetch all parcel delivery orders |

Open the browser to view the endpoints with their specifications
* localhost:5000 


## Contributors
- [Steven Opio](https://github.com/steveviko)

## This Platform is served by  
- Git-pages [GitHub Pages](https://steveviko.github.io/SendIT/UI/index.html). 

## Demo
- The API is hosted [Here](https://venvikosendit.herokuapp.com/api/v1/parcels)

## MIT License

Copyright (c) 2018 **VenViko**