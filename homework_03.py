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

# min = int(input("Enter the minimum number (between 1 and 999): ")) # Test input for "min"
# max = int(input("Enter the maximum number (between 2 and 1000): ")) # Test input for "max"
# quantity = int(input("Enter the quantity of numbers to generate: ")) # Test input for "quantity"

import random
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or max <= min or quantity > (max - min + 1):
        return []
    else:
        numbers = random.sample(range(min, max + 1), quantity)
        return sorted(numbers)
  
# print(f"Function returns: {get_numbers_ticket(min, max, quantity)}") # function testrun to verify the result

# Task 3:

def normalize_phone(phone_number)
    pass

    


