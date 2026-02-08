# Task 1: Generating a function that calculates the number of days from given date to today.

# date = input("Enter a date formatted as YYYY-MM-DD: ") # input for testing the function execution

from datetime import datetime
def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        delta_days = today - given_date
        return delta_days.days
    except ValueError: 
        return "Invalid date format. Please use YYYY-MM-DD format."

# print(f"Here's the end result of the task: {get_days_from_today(date)}") # result output for testing


# Task 2:




