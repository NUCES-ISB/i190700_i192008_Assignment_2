from flask import Flask, jsonify, render_template, request
from flask_dotenv import DotEnv
from utils.weather.open_weather import get_max_and_min_temperature
from utils.weather.weather_stack import get_precipitation_and_wind_speed
from utils.model.model import weather_predictor
import requests
import threading

app = Flask(__name__)
env = DotEnv(app)
env.init_app(app)

@app.route('/')
def get_weather():
    try:
        # Weatherstack API for Precepitation
        # OpenWeather API for Min/Max temperature and wind speed
        weatherstack_api_key = app.config['WEATHERSTACK_API_KEY']
        openweather_api_key = app.config['OPENWEATHER_API_KEY']

        lat = 33.738045
        lon = 73.084488
        location = "Islamabad"

        precipitation, windSpeed = get_precipitation_and_wind_speed(weatherstack_api_key, location)
        maxTemp, minTemp = get_max_and_min_temperature(openweather_api_key, lat, lon) 

        # Remove this line later
        # input=[[1.140175,8.9,2.8,2.469818]]
        # predValue = weather_predictor.predict(input)
        predValue = weather_predictor.predict([[precipitation, maxTemp, minTemp, windSpeed]])

        prediction = ""
        if(predValue==0):
            prediction = "Drizzle"
        elif(predValue==1):
            prediction = "Fog"
        elif(predValue==2):
            prediction = "Rain"
        elif(predValue==3):
            prediction = "Snow"
        else:
            prediction = "Sun"


        # 

        # return jsonify({ "Location":location, "Precipitation": precipitation, "WindSpeed": windSpeed, "MaxTemp": maxTemp, "MinTemp": minTemp})
        return render_template('index.html', precipitation=precipitation, wind_speed=windSpeed, max_temp=maxTemp, min_temp=minTemp, prediction=prediction)

    except Exception as e:
        return jsonify({'error':e})
    

@app.route('/form', methods=['POST', 'GET'])
def predictFromInput():
    if (request.method == 'POST'):
        precipitation = float(request.form['precipitation'])
        wind_speed = float(request.form['wind_speed'])
        max_temp = float(request.form['max_temp'])
        min_temp = float(request.form['min_temp'])

        predValue = weather_predictor.predict([[precipitation, max_temp, min_temp, wind_speed]])

        prediction = ""
        if(predValue==0):
            prediction = "Drizzle"
        elif(predValue==1):
            prediction = "Fog"
        elif(predValue==2):
            prediction = "Rain"
        elif(predValue==3):
            prediction = "Snow"
        else:
            prediction = "Sun"

        return render_template('form.html', prediction=prediction)

    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)