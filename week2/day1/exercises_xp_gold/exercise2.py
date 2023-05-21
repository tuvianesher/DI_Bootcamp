month = int(input("Enter a month (1 to 12): "))

if month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
elif month in [9, 10, 11]:
    season = "Autumn"
else:
    season = "Winter"

print(f"The season of month {month} is {season}.")
