from datetime import datetime, timedelta

current_date = datetime.now()
print("Today's date is:", current_date)

one_day = timedelta(days=1)
yesterday_date = current_date - one_day
print("Yesterday's date is:", yesterday_date)
print("Tomorrow's date is:", current_date + one_day)

# Input date in correct format
date_input = input("Enter a date in YYYY-MM-DD format: ")

# Parse the input date correctly
date = datetime.strptime(date_input, '%Y-%m-%d')

# Calculate one week later
one_week = timedelta(weeks=1)
one_week_later = date + one_week

print("One week later it will be:", one_week_later)
