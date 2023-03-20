import requests

def get_precipitation_and_wind_speed(api_key, location):
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={location}'
    try:
        response = requests.get(url)
        # print(f"Weather Stack Response:\n{response}")

        data = response.json()
        # print(data)
        precipitation = data['current']['precip']
        wind_speed = data['current']['wind_speed']
        return precipitation, wind_speed
    
    except ValueError as v:
        raise ValueError(v)
    
    except Exception as e:
        raise Exception(e)
        
    