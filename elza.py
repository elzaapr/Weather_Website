from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Ganti dengan API key yang didapat dari OpenWeatherMap
API_KEY = '2a6efd300f9caac34c8e485a7c82d162'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(city):
    # Membuat URL untuk API request
    url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        main_data = data['main']
        weather_data = data['weather'][0]
        return {
            'city': city,
            'temperature': main_data['temp'],
            'pressure': main_data['pressure'],
            'humidity': main_data['humidity'],
            'description': weather_data['description'],
            'icon': weather_data['icon']
        }
    else:
        return None


@app.route('/', methods=['GET', 'POST'])
def home():
    weather_info = None
    if request.method == 'POST':
        city = request.form['city']
        weather_info = get_weather(city)
    return render_template('index.html', weather_info=weather_info)


@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    weather_info = get_weather(city)
    if weather_info:
        return jsonify(weather_info)
    else:
        return jsonify({'error': 'City not found!'})


if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Menggunakan port 5001