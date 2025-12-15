from datetime import datetime
#TODO: this is a mock calendar event, will get data from api after
def get_todays_events():
    return [
        {
            "title": "Meet Alex",
            "start_time": "2025-12-15T16:00:00",
            "location": "Central London",
            "is_outside": True
        },
        {
            "title": "Gym",
            "start_time": "2025-12-15T19:00:00",
            "location": "Local gym",
            "is_outside": True
        }
    ]
