# This script will demonstrate your ability to use the datetime module for 
# handling dates and times in Python.

from datetime import datetime, timedelta

def display_current_datetime():
    x = datetime.now()
    return x.strftime("%Y-%m-%d %H:%M:%S")

current_date = display_current_datetime()
print(f"Current date and time: {current_date}")

days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(days):
    return current_date + timedelta(days=days)

future_date = calculate_future_date(days)
print(future_date.strftime("%Y-%m-%d"))
