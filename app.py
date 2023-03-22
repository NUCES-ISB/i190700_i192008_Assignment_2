from flask import Flask, jsonify, render_template, request
from flask_dotenv import DotEnv
from datetime import datetime
from utils.weather.current_weather import currentWeather
from utils.weather.today_weather import todayWeather
from utils.model.model import weather_predictor

app = Flask(__name__)
env = DotEnv(app)
env.init_app(app)

@app.route('/')
def get_weather():
    try:
        time = datetime.now()
        api_key = app.config['WEATHER_API']

        location = "Islamabad"

        currentWeatherData = currentWeather(api_key, location)
        todaysWeatherData = todayWeather(api_key, location)

        precipitation = currentWeatherData["current"]["precip_in"]
        windSpeed = currentWeatherData["current"]["wind_kph"]
        maxTemp = todaysWeatherData["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
        minTemp = todaysWeatherData["forecast"]["forecastday"][0]["day"]["mintemp_c"]

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


        return render_template('index.html', precipitation=precipitation, wind_speed=windSpeed, max_temp=maxTemp, min_temp=minTemp, prediction=prediction, time=time)

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