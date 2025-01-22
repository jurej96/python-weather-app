"""
This Python Weather App simulates a weather forecast for a given city using hardcoded weather data.
It:
1. Displays a welcome message.
2. Asks the user for a city name.
3. Fetches weather data from a hardcoded dictionary.
4. Displays current temperature, conditions, wind speed, and humidity.
5. Validates the city name against the hardcoded dataset.
6. Allows the user to choose temperature in Celsius or Fahrenheit.
7. Displays a thank you message before exiting.
"""

def celsius_to_fahrenheit(celsius_value):
    """
    Convert Celsius to Fahrenheit using the formula (C x 9/5) + 32.
    """
    return (celsius_value * 9/5) + 32

# Hardcoded weather data for various cities, storing the temperature in Celsius (as integers).
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
    "Tokyo": {
        "temperature": 18, 
        "conditions": "Rainy", 
        "wind_speed": "7 km/h", 
        "humidity": "90%"
    },
    "Sydney": {
        "temperature": 22, 
        "conditions": "Windy", 
        "wind_speed": "15 km/h", 
        "humidity": "60%"
    },
    "Paris": {
        "temperature": 17, 
        "conditions": "Foggy", 
        "wind_speed": "3 km/h", 
        "humidity": "85%"
    },
    "Berlin": {
        "temperature": 16,
        "conditions": "Cloudy",
        "wind_speed": "4 km/h",
        "humidity": "70%"
    },
    "Cairo": {
        "temperature": 30,
        "conditions": "Sunny",
        "wind_speed": "5 km/h",
        "humidity": "40%"
    },
    "Toronto": {
        "temperature": 10,
        "conditions": "Rainy",
        "wind_speed": "6 km/h",
        "humidity": "75%"
    }
}

def display_weather(city_name, unit="C"):
    """
    Display weather data for a specified city in Celsius or Fahrenheit.

    Args:
        city_name (str): The name of the city.
        unit (str): The desired temperature unit ('C' for Celsius, 'F' for Fahrenheit).
    """
    city_data = weather_data[city_name]

    # Convert the temperature if user chooses Fahrenheit
    if unit.upper() == "F":
        # Use .1f format specifier for one decimal place
        converted_temp = celsius_to_fahrenheit(city_data["temperature"])
        temperature_str = f"{converted_temp:.1f}°F"
    else:
        temperature_str = f"{city_data['temperature']}°C"

    # Print weather details
    print(f"\nWeather forecast for {city_name}:")
    print(f"Temperature: {temperature_str}")
    print(f"Conditions: {city_data['conditions']}")
    print(f"Wind speed: {city_data['wind_speed']}")
    print(f"Humidity: {city_data['humidity']}\n")

def main():
    """
    Main function that orchestrates the flow of the weather application.
    """
    # 1. Display a welcome message
    print("Welcome to the Python Weather App!")

    # Display the available cities so the user knows valid inputs
    print("\nAvailable cities:")
    for city in weather_data:
        print(f"- {city}")

    # 2. Ask for the city name
    city_name = input("\nEnter the city name for which you need the weather forecast: ")

    # 3. Validate user input; re-prompt if city not in the hardcoded list
    while city_name not in weather_data:
        print("Invalid city name. Please try again.")
        city_name = input("Enter a valid city from the list: ")

    # Prompt user for temperature unit preference (Celsius or Fahrenheit)
    unit = input("Would you like the temperature in Celsius (C) or Fahrenheit (F)? ")
    while unit.upper() not in ["C", "F"]:
        print("Invalid choice. Please enter either 'C' or 'F'.")
        unit = input("Would you like the temperature in Celsius (C) or Fahrenheit (F)? ")

    # 4. Fetch weather data (done implicitly from weather_data) and display
    display_weather(city_name, unit)

    # 6. Display a thank you message
    print("Thank you for using the weather forecast application!")

# Entry point of the program
if __name__ == "__main__":
    main()