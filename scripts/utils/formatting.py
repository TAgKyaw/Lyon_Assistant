def build_greeting_message(username, weather, transit, events):
    # Simple version — we'll improve with better natural phrasing
    event_lines = []
    for e in events:
        event_lines.append(f"- {e['title']} at {e['time']} ({e.get('location', 'no location')})")

    events_str = "\n".join(event_lines)

    return (
        f"Good day, {username}.\n"
        f"Weather: {weather['condition']} and {weather['temp_c']}°C.\n"
        f"Transit: {transit['status'].capitalize()} ({transit['reason']}).\n\n"
        f"Today's agenda:\n{events_str}"
    )
