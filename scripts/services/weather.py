# services/weather.py
import requests
from typing import Dict

WEATHER_URL = "https://api.weatherapi.com/v1/current.json"

class WeatherServiceError(Exception):
    pass


def get_weather_summary(location: Dict, api_key: str) -> Dict:
    """
    Fetch current weather and return normalized summary.
    """
    params = {
        "key": api_key,
        "q": f"{location['lat']},{location['lon']}"
    }

    try:
        response = requests.get(WEATHER_URL, params=params, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        raise WeatherServiceError(f"Weather API request failed: {e}")

    data = response.json()

    # ---- Normalization layer ----
    try:
        return {
            "city": data["location"]["name"],
            "condition": data["current"]["condition"]["text"].lower(),
            "temp_c": round(data["current"]["temp_c"]),
            "feels_like_c": round(data["current"]["feelslike_c"]),
            "wind_kph": round(data["current"]["wind_kph"])
        }
    except KeyError as e:
        raise WeatherServiceError(f"Unexpected weather API response format: {e}")
