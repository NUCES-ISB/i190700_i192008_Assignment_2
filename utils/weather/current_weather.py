import requests

def currentWeather(api_key, location):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"

    try:
        response = requests.get(url)

        data = response.json()

        return data
    
    except ValueError as v:
        raise ValueError(v)
    
    except Exception as e:
        raise Exception(e)