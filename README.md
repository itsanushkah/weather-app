# 🌦️ Weather App

A sleek Flask-based weather app that shows real-time weather for any city using the [OpenWeatherMap API](https://openweathermap.org/api). Features an animated weather-based background, a rotating Earth globe, and a clean, responsive UI.

## Features

- Real-time weather lookup for any city worldwide
- Current temperature, "feels like" temperature, humidity, and condition description
- Local time at the searched city, computed from the city's UTC offset
- Animated rotating Earth globe and weather-condition backgrounds
- Friendly error handling for unknown/invalid city names

## Tech stack

- **Backend:** Python, Flask
- **Weather data:** OpenWeatherMap API
- **Frontend:** HTML/CSS (Jinja templates), animated GIF background
- **Config:** `python-dotenv` for local environment variables

## Project structure

```
.
├── app.py              # Flask app + OpenWeatherMap request/response handling
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Search form + weather results UI
└── static/
    └── Rotating_earth_animated_transparent.gif
```

## Running locally

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api) and add it to a `.env` file in the project root:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000` and search for a city.

## How it works

The app takes a city name from a simple form, calls the OpenWeatherMap current-weather endpoint, and renders the temperature, conditions, humidity, and the city's local time (converted from the API's UTC timestamp + timezone offset) back into the page — along with a matching animated background.
