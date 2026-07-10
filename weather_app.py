import tkinter as tk
from tkinter import ttk
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

api_key = API_KEY

# --- Logic ---

def get_weather():
    city = entry.get()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        result_label.config(text="City not found")
        return

    temp = data["main"]["temp"]
    condition = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    result_label.config(text=f"{temp}°C, {condition}, {humidity}% humidity")

# --- User interface ---

root = tk.Tk()
root.title("Weather")
root.geometry("250x150")

entry = ttk.Entry(root)
entry.pack(pady=10)

button = ttk.Button(root, text="Search", command=get_weather)
button.pack()

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()