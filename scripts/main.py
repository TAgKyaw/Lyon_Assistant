from config import USER_CONFIG
from services.weather import get_weather_summary
from services.transit import get_transit_summary
from services.calendar import get_todays_events
from services.system import get_username
from utils.formatting import build_greeting_message

def main():
    username = get_username()
    location = USER_CONFIG["location"]
    commute = USER_CONFIG["commute"]
    
    # weather_info = get_weather_summary(location)
    weather = get_weather_summary(
        location=USER_CONFIG["location"],
        api_key=USER_CONFIG["weather"]["api_key"]
    )
    transit_info = get_transit_summary(commute)
    events = get_todays_events()

    # message = build_greeting_message(
    #     username=username,
    #     weather=weather,
    #     transit=transit_info,
    #     events=events
    # )

    # print(message)
    print(weather)

if __name__ == "__main__":
    main()
