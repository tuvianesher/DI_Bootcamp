import datetime

def minutes_lived(birthdate):
    current_datetime = datetime.datetime.now()
    birth_datetime = datetime.datetime.strptime(birthdate, "%Y-%m-%d")  # Convert birthdate string to datetime object
    time_lived = current_datetime - birth_datetime

    minutes = int(time_lived.total_seconds() / 60)

    print(f"You have lived approximately {minutes} minutes.")

# You can test the function by calling it with a birthdate
birthdate = "1990-05-15"  # Example birthdate in the format "YYYY-MM-DD"
minutes_lived(birthdate)
