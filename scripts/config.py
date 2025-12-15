from dotenv import load_dotenv
import os

load_dotenv()

USER_CONFIG = {
    "location": {
        "city": "London",
        "lat": 51.5072,
        "lon": -0.1276
    },
    "commute": {
        "from": "Feltham",
        "to": "Waterloo",
        "lines": ["Northern", "Central"]
    },
    "calendar": {
        "provider": "google",
        "calendar_id": "primary"
    },
    "weather" : {
        "api_key": os.getenv('WEATHER_API_KEY')
    },
    "tfl": {
        "app_id": os.getenv('TFL_APP_ID'),
        "app_key": os.getenv('TFL_APP_KEY')
    },
    "gemini": {
        "api_key": os.getenv('GEMINI_API_KEY')
    }
}
