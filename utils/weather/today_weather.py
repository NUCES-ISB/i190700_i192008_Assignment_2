import requests
from datetime import datetime


def todayWeather(api_key, location):
    today = datetime.today().strftime("%Y-%m-%d")
    url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={location}&dt={today}"

    try:
        response = requests.get(url)

        data = response.json()

        return data
    
    except ValueError as v:
        raise ValueError(v)
    
    except Exception as e:
        raise Exception(e)