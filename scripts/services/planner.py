# services/planner.py
from typing import List, Dict
from datetime import datetime

def build_day_plan(events: List[Dict], weather_info: Dict) -> List[Dict]:
    """
    Processes the day's events and the weather forecast to generate actionable reminders.
    
    Args:
        events: A list of today's events from calendar.py.
        weather_info: The weather summary from weather.py.
        
    Returns:
        A list of reminder dictionaries.
    """
    reminders = []
    
    # Extract the current weather summary for use in reminders
    weather_summary = weather_info.get("summary", "Weather details unavailable.")
    
    for event in events:
        # 1. Format the time
        try:
            # Parse the ISO format string (e.g., "2025-12-15T16:00:00")
            dt_object = datetime.fromisoformat(event['start_time'])
            # Format to a friendly 12-hour time string
            time_str = dt_object.strftime("%I:%M %p") 
        except ValueError:
            time_str = "Time TBA"
        
        # 2. Determine the weather note
        weather_note = ""
        if event.get('is_outside'):
            # This is the key planning logic: advise on outdoor events
            weather_note = f"⚠️ IMPORTANT: This is an outdoor event. Expect: {weather_summary}"
        
        # 3. Create the final reminder object
        reminders.append({
            "event": event['title'],
            "time": time_str,
            "location": event['location'],
            "weather_note": weather_note
        })
        
    return reminders