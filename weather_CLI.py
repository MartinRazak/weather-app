import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

city = input("Enter city: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

# Check if the city exists
if response.status_code != 200:
    print("Error:", data.get("message", "Unable to retrieve weather data."))
    exit()

temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
weather = data["weather"][0]["description"]

print(f"\nWeather in {city.title()}:")
print(f"Temperature: {temp} °C")
print(f"Humidity: {humidity}%")
print(f"Condition: {weather}")

# Small feature: Weather advice
# print("\nAdvice:")
# if "rain" in weather.lower():
#     print("🌧️ Don't forget your umbrella!")
# elif temp < 10:
#     print("🧥 It's cold outside. Wear a jacket!")
# elif temp > 30:
#     print("🥵 Stay hydrated and avoid the midday sun.")
# else:
#     print("😊 The weather looks pleasant. Have a great day!")