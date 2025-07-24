# This script will demonstrate your ability to use the datetime module for 
# handling dates and times in Python.

import datetime

def display_current_datetime():
    return datetime.datetime.now("%Y-%m-%d %H:%M:%S")

current_date = display_current_datetime()
print(current_date)

days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(days):
    change = datetime.timedelta(days=days)
    return current_date + change

future_date = calculate_future_date(days)
print(future_date.date())
