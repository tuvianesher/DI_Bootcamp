from datetime import datetime

def display_today_and_upcoming_holiday():
    # Get today's date
    today = datetime.now().date()
    print("Today's Date:", today)

    # Get the next upcoming holiday
    upcoming_holiday = datetime(year=today.year, month=12, day=25).date()  # Example: Christmas on December 25
    if today > upcoming_holiday:
        upcoming_holiday = datetime(year=today.year+1, month=12, day=25).date()

    # Calculate the time left until the upcoming holiday
    time_left = upcoming_holiday - today
    print("Next Holiday:", upcoming_holiday.strftime("%B %d"))
    print("Time Left until Next Holiday:", time_left)

display_today_and_upcoming_holiday()
