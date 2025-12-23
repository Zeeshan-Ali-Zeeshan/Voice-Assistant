import requests
import json
from body.speak import speak

def get_temperature_weatherapi(city):
    api_key = "bc6f245df34c4c9e870111727240608"  # Replace with your WeatherAPI key
    endpoint = "https://api.weatherapi.com/v1/current.json"

    try:
        # Send GET request
        response = requests.get(endpoint, params={"key": api_key, "q": city})

        # Check if request was successful
        if response.status_code == 200:
            data = json.loads(response.text)

            # Extract temperature in Celsius
            if "current" in data and "temp_c" in data["current"]:
                return data["current"]["temp_c"]
            else:
                print("Error: Temperature data not found in response.")
        else:
            print(f"Error: Failed to fetch data from API. Status code: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred: {e}")

    return None

def Temp():
    city = "Burewala"  # You can change or dynamically set this
    temperature_celsius = get_temperature_weatherapi(city)

    if temperature_celsius is not None:
        speak(f"The weather in {city} is {temperature_celsius}°C")
    else:
        speak("Sorry, I couldn't retrieve the weather data.")

