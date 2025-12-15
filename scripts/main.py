from config import USER_CONFIG
from services.weather import get_weather_summary
from services.transit import get_transit_summary
from services.calendar import get_todays_events
from services.system import get_username
# from utils.formatting import build_greeting_message #this is replaced with generate_planner_summary()
from services.planner import build_day_plan
from services.llm import generate_planner_summary

def main():
    username = get_username()
    location = USER_CONFIG["location"]
    commute = USER_CONFIG["commute"]
    
    weather = get_weather_summary(
        location=USER_CONFIG["location"],
        api_key=USER_CONFIG["weather"]["api_key"]
    )
    # transit_info = get_transit_summary(commute) we do not need transit data for now
    events = get_todays_events()
    reminders = build_day_plan(events, weather)

    # Convert reminders (list of dictionaries) into a readable string 
    # for the LLM. We will include Weather and Transit data here too.
    context_data = {
        "Weather": weather,
        # "Transit": transit_info,
        "Reminders": reminders
    }
    
    # --- NEW LLM CALL ---
    summary_message = generate_planner_summary(
        api_key=USER_CONFIG["gemini"]["api_key"],
        name=username,
        reminders=context_data # Pass all the context data
    )
    
    # Print the final, AI-generated message
    print(summary_message)

if __name__ == "__main__":
    main()
