from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("WEATHER_API_KEY")  # stored in .env file

@app.route("/", methods=["GET", "POST"])
def index():
    weather = {}

    if request.method == "POST":
        city = request.form.get("city")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] != 200:
                weather["error"] = f"City '{city}' not found."
            else:
                weather["city"] = data["name"]
                weather["desc"] = data["weather"][0]["description"]
                weather["temp"] = round(data["main"]["temp"], 2)
                weather["feels_like"] = round(data["main"]["feels_like"], 2)
                weather["humidity"] = data["main"]["humidity"]
                weather["main"] = data["weather"][0]["main"].lower()
                weather["icon"] = data["weather"][0]["icon"]

                # Convert UTC timestamp to local time using city's timezone offset
                utc_time = datetime.utcfromtimestamp(data["dt"])
                local_time = utc_time + timedelta(seconds=data["timezone"])
                weather["time"] = local_time.strftime("%Y-%m-%d %H:%M:%S") + " (Local Time)"

        except Exception as e:
            weather["error"] = "An error occurred. Please try again later."

    return render_template("index.html", weather=weather)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
