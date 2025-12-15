# services/calendar.py (UPDATED)
import json
import datetime
from typing import List, Dict

# The file containing our mock data
MOCK_FILE_NAME = f'../data/mock_events.json'

def get_todays_events() -> List[Dict]:
    """
    Reads all events from the mock JSON file and filters for today's events.
    The calendar_id parameter is now ignored but kept for future API compatibility.
    """
    try:
        with open(MOCK_FILE_NAME, 'r') as f:
            all_events = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: Mock data file '{MOCK_FILE_NAME}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"ERROR: Could not decode JSON from '{MOCK_FILE_NAME}'. Check file format.")
        return []

    # Get today's date for comparison
    today = datetime.date(2025, 12, 15) # For consistent testing, we'll hardcode today's date
    # today = datetime.date.today() # Use this when you are running it normally

    todays_events = []
    for event in all_events:
        try:
            # Extract only the date part of the ISO string (e.g., "2025-12-15")
            event_date_str = event['start_time'].split('T')[0]
            event_date = datetime.datetime.strptime(event_date_str, '%Y-%m-%d').date()
            
            if event_date == today:
                todays_events.append(event)
        except (KeyError, ValueError) as e:
            print(f"Skipping event with bad format: {event}. Error: {e}")
            continue

    return todays_events