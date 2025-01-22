# Python Weather App

## Overview
The **Python Weather App** is a simple command-line tool that simulates a weather forecast for a given city using hardcoded weather data. This project showcases Python basics, including user input handling, dictionary-based data storage, and data validation. It’s a great starting point for beginners looking to build interactive Python applications.

## Features
- Displays a welcome message to the user.
- Lists available cities for weather forecasts.
- Prompts the user to enter a city name and validates it against the dataset.
- Fetches weather data (temperature, conditions, wind speed, and humidity) from a hardcoded dictionary.
- Allows the user to choose the temperature unit: **Celsius (°C)** or **Fahrenheit (°F)**.
- Provides a thank-you message before exiting.

## How It Works
1. The program welcomes the user and displays the list of available cities.
2. The user enters the name of a city for which they want the weather forecast.
3. The app validates the city name against the hardcoded dataset.
4. The user selects the temperature unit (Celsius or Fahrenheit).
5. The app displays:
   - Current temperature (in the chosen unit),
   - Weather conditions,
   - Wind speed,
   - Humidity.
6. The app thanks the user before exiting.

## Example Weather Data
The weather data is stored in a Python dictionary. Below are example entries:

```python
weather_data = {
    "London": {
        "temperature": 15, 
        "conditions": "Cloudy",
        "wind_speed": "5 km/h", 
        "humidity": "80%"
    },
    "New York": {
        "temperature": 20, 
        "conditions": "Sunny", 
        "wind_speed": "10 km/h", 
        "humidity": "50%"
    },
}
