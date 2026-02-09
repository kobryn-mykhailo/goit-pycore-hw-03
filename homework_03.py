# Task 1:

# Testing input for Task 1
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

# Testing
# print(f"Here's the end result of the task: {get_days_from_today(date)}") # result output for testing


# Task 2:

# Testing inputs for Task 2
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

# Testing
# print(f"Function returns: {get_numbers_ticket(min, max, quantity)}") # function testrun to verify the result

# Task 3:

import re

def normalize_phone(phone_number):
    cleaned_phone = re.sub(r'[^+\d]', '', phone_number)
    if cleaned_phone.startswith("+"):
        return cleaned_phone
    elif cleaned_phone.startswith("380"):
        return "+" + cleaned_phone
    elif cleaned_phone.startswith("0"):
        return "+38" + cleaned_phone
    else:
        return "+380" + cleaned_phone
    
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# Testing
# print(f"Normalized phone numbers for SMS: {sanitized_numbers}") # testing the output of the function that sanityzes the phone numbers

# Task 4:

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until = (birthday_this_year - today).days
        
        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year
            
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)

            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)
            
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming

# Testing
# users = [
#     {"name": "John Doe", "birthday": "1985.02.13"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]

# print(get_upcoming_birthdays(users)) # testing the function operability with a sample dictionary of users with birthdays


