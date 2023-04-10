from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        # Default city
        city = 'New York'

    # API call to OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=11795e0d12bfca5dffc68c9245722f6e'
    response = requests.get(url)
    data = json.loads(response.text)
    if 'weather' not in data:
        error_msg = f"No weather information found for '{city}'. Please enter a valid city name."
        return render_template('weather.html', error=error_msg)
    # Extract relevant weather data
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
    humidity = data['main']['humidity']

    return render_template('weather.html', city=city, weather_description=weather_description,
                           temperature=temperature, humidity=humidity)

if __name__ == '__main__':
    app.run(debug=True)
   