import pickle
import os

def load_weather_predictor():
    model_file = os.path.join(os.path.dirname(__file__), 'weather_predictor')
    with open(model_file, 'rb') as f:
        weather_predictor = pickle.load(f)
    return weather_predictor

weather_predictor = load_weather_predictor()