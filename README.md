# Machine Learning App Deployment

This repository contains the code for deploying a machine learning model that predicts whether a customer will book a flight or not. The model is trained on a dataset provided by a major airline company and uses a Decision Tree classifier algorithm.

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

## Deployment

To deploy the app, follow these steps:

1. Clone this repository to your local machine.
2. Install Docker on your machine if you don't have it already.
3. Build the Docker image by running `docker build -t ml-app .` in the root directory of the repository.
4. Run the Docker container by running `docker run -p 8000:8000 ml-app`.
5. The app should now be running and accessible at `http://localhost:8000`.

## Usage

To use the app, send a POST request to the `/predict` endpoint with a JSON payload containing the customer data. The app will return a prediction of whether the customer will book a flight or not.

## Testing

To run the tests, install Tox and run `tox` in the root directory of the repository. This will run the tests using Pytest and check that everything is working correctly.
