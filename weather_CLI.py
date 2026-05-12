import requests

city = input("Enter city: ")

api_key = "cbbcee4ec9745cbcf38e772b52daae49"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print(data)

temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
weather = data["weather"][0]["description"]

print(f"\nWeather in {city}:")
print("Temperature:", temp, "°C")
print("Humidity:", humidity, "%")
print("Condition:", weather)