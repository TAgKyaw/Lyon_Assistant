Project Scaffolding

assistant/
│
├── main.py                   # Entry point: greets user, coordinates features
│
├── config.py                 # User settings: location, commute routes, calendar ID
│
├── services/
│   ├── weather.py            # Fetch weather (OpenWeather / MetOffice / etc.)
│   ├── transit.py            # Fetch transit data (TFL API or GTFS proxy)
│   ├── calendar.py           # Get today's events (Google/Outlook API)
│   └── system.py             # Local system info (time, username)
│
├── utils/
│   ├── formatting.py         # Helper to build natural-sounding messages
│   └── time_helpers.py       # Convert times, formats, durations
│
└── README.md


🧭 How this scaffold maps to the developer
✔ Greets the user

system.get_username() + formatter → greeting text.

✔ Fetches weather

weather.get_weather_summary() → currently mocked, but structure is ready.

✔ Fetches transit delays

transit.get_transit_summary() → when we hook into TFL, this becomes real.

✔ Reads calendar events

calendar.get_todays_events() → can connect to Google or Outlook API later.

✔ Produces a natural message

formatting.build_greeting_message() → we will later replace with LLM-generated phrasing if you want.
