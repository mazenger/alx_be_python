from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    current_date = now.date()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current Date: {current_date}")
    print(f"Current Date and Time: {formatted_datetime}")

    # Example of timedelta: show date/time 1 day ahead
    one_day_later = now + timedelta(days=1)
    print(f"Date and Time one day later: {one_day_later.strftime('%Y-%m-%d %H:%M:%S')}")
