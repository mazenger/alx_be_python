from datetime import datetime

def display_current_datetime():

    now = datetime.now()
    current_date = now
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current Date: {current_date}")
    print(f"Current Date and Time: {formatted_datetime}")

# Example usage:
display_current_datetime()