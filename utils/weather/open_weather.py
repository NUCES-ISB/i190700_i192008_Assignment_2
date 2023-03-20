import requests

def get_max_and_min_temperature(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        
        # print(f"Open Weather Response:\n{response}")

        data = response.json()
        # print(data)
        
        max_temp = data["main"]["temp_max"]
        min_temp = data["main"]["temp_min"]
        return max_temp, min_temp
    
    except ValueError as v:
        raise ValueError(v)
    
    except Exception as e:
        raise Exception(e)