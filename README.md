# ATP Rankings API

## Overview
This Flask application is designed to scrape and provide ATP (Association of Tennis Professionals) Tour rankings data via a simple API. It fetches information about tennis players' rankings from the official ATP Tour website and allows users to query specific player details based on their ranking.

## Features
- **Web Scraping**: Extracts player data from the ATP Tour's official rankings page.
- **REST API**: Users can retrieve information about a player by specifying their ATP ranking.
- **Player Data**: For each player, the API provides details such as name, age, and ATP points.

## How It Works
The application scrapes the ATP Tour rankings page and parses the data into a structured format. It provides an endpoint where users can request data for a player based on their ATP ranking. The returned data includes the player's name, age, and the number of ATP points they currently have.

## Usage
To use the API, send a GET request to the endpoint with the desired player's rank as a query parameter. For example: `http://localhost:5000/get_player_by_rank?rank=10` would return the information for the player currently ranked 10th in the ATP rankings.

## Development and Deployment
This project is developed using Flask, a lightweight WSGI web application framework in Python. It's designed to be easy to use and straightforward to deploy to a production environment.
