from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)
API_KEY = 'xxxxxxxxxxxxxx'  # Replace with your actual OpenWeatherMap API key

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        base_url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(base_url, params=params)
        data = response.json()

        print(f"\nDEBUG: API response for {city} → {data}\n")

        if response.status_code == 200:
            weather = {
                'city': data['name'],
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'desc': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'main': data['weather'][0]['main'].lower(),  # <— lowercase fix
                'time': datetime.now().strftime('%I:%M %p, %d %b %Y')
            }
        else:
            weather = {'error': f"City '{city}' not found."}

    return render_template('index.html', weather=weather)

import os

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

