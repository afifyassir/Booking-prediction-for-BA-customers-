# Machine Learning App Deployment

This repository contains the code for deploying a machine learning model that predicts whether a customer will book a flight or not. The model is trained on a dataset provided by a major airline company and uses a Decision Tree classifier algorithm.

## Features used 
- num_passengers = number of passengers travelling
- sales_channel = sales channel booking was made on
- trip_type = trip Type (Round Trip, One Way, Circle Trip)
- purchase_lead = number of days between travel date and booking date
- length_of_stay = number of days spent at destination
- flight_hour = hour of flight departure
- flight_day = day of week of flight departure
- route = origin -> destination flight route
- booking_origin = country from where booking was made
- wants_extra_baggage = if the customer wanted extra baggage in the booking
- wants_preferred_seat = if the customer wanted a preferred seat in the booking
- wants_in_flight_meals = if the customer wanted in-flight meals in the booking
- flight_duration = total duration of flight (in hours)
- booking_complete = flag indicating if the customer completed the booking

## Tools and Libraries

The app is built using several tools and libraries, including:

- FastAPI: for building the web API
- Pydantic: for data validation and settings management
- Uvicorn: for running the app
- Loguru: for logging
- Typing: for type annotations
- Docker: for containerization
- Tox: for testing and automation
- Pytest: for testing
- flake8: for code linting
- black: for code formatting

## Usage

To use the app, send a POST request to the `/predict` endpoint with a JSON payload containing the customer data. The app will return a prediction of whether the customer will book a flight or not.

## Testing

To run the tests, install Tox and run `tox` in the root directory of the repository. This will run the tests using Pytest and check that everything is working correctly.
