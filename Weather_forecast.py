import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import requests

DEFAULT_API_KEY = "d00a38e359d71ae91847e4598e8f571f"

def get_weather(location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': DEFAULT_API_KEY,
        'units': 'metric'  # You can use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            return None
    except requests.ConnectionError:
        return None

def display_weather():
    location = location_entry.get()
    weather_data = get_weather(location)

    if weather_data:
        city_label.config(text=f"City: {weather_data['name']}")
        temp_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
        humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
        wind_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} m/s")
        desc_label.config(text=f"Description: {weather_data['weather'][0]['description']}")
        status_label.config(text="")
    else:
        status_label.config(text="Error: Unable to retrieve weather information.")

# Create the main window
app = tk.Tk()
app.title("Weather Forecast App")

# Apply themed style
style = ThemedStyle(app)
style.set_theme("arc")  # You can choose different themes

# Location entry
location_label = ttk.Label(app, text="Enter the name of a city or a zip code:")
location_label.pack(pady=10)
location_entry = ttk.Entry(app, font=('Arial', 12))
location_entry.pack(pady=10)

# Display weather button
weather_button = ttk.Button(app, text="Get Weather", command=display_weather)
weather_button.pack(pady=20)

# Weather information labels
city_label = ttk.Label(app, text="", font=('Arial', 14, 'bold'))
city_label.pack(pady=10)
temp_label = ttk.Label(app, text="", font=('Arial', 12))
temp_label.pack(pady=5)
humidity_label = ttk.Label(app, text="", font=('Arial', 12))
humidity_label.pack(pady=5)
wind_label = ttk.Label(app, text="", font=('Arial', 12))
wind_label.pack(pady=5)
desc_label = ttk.Label(app, text="", font=('Arial', 12))
desc_label.pack(pady=5)
status_label = ttk.Label(app, text="", font=('Arial', 12, 'italic'))
status_label.pack(pady=20)

# Run the application
app.mainloop()
