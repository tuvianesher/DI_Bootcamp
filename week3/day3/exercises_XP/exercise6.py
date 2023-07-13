import datetime

def time_left_until_january():
    current_date = datetime.datetime.now()
    january_1st = datetime.datetime(current_date.year + 1, 1, 1)  # Next year's January 1st
    time_left = january_1st - current_date

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"The 1st of January is in {days} days, {hours}:{minutes:02d}:{seconds:02d} hours.")

# You can test the function by calling it
time_left_until_january()
