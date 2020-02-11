

# my_date
#   -- date_operations.py
#   -- __init__.py
#      1. get_current_datetime
#      2. When entering age in string: 19 years, 5 months, 20 days. It should 
#      return birth_date
#      3. When entering birth_date. Return age in the above format.
#      4. When entering birth_date: Return how many time will person take to 
#      turn 50 years. Return string in above format.

from datetime import datetime, timedelta
from dateutil import relativedelta

def get_current_datetime():
    return datetime.today()


def birth_date(age):
    # extracting years, months and days from the age string
    age = "".join(char if char.isdigit() else " " for char in age).split()
    years = int(age[0])
    months = int(age[1])
    days = int(age[2])

    # # calculating total days
    # total_days = (years*12 + months)*30 + days

    # # get current date and time
    # today = get_current_datetime()

    # # calculating previous date based on total_days
    # birth_date = today - timedelta(days=total_days)

    today = get_current_datetime()
    weeks = (years + months/12) * 52
    birth_date = today - timedelta(weeks= weeks, days=days)
    print(birth_date)

    # formating birth_date in string
    birth_date = "{0}-{1}-{2}".format(birth_date.year, birth_date.month, birth_date.day)
    
    return birth_date


birth_date("22 years, 5 months, 2 days")

def get_age(year, month, day):
    # get current date and time
    today = get_current_datetime()

    # birth year, month, day to datetime class
    birth_date = datetime(year, month, day)

    # calculating relative difference between current date and birth date
    age = relativedelta.relativedelta(today, birth_date)
   
    # making string with years, months, and days
    age = "{0} years, {1} months, {2} days".format(age.years, age.months, age.days)
    
    # returning string
    return age

def time_until_50(year, month, day):
    today = datetime.today() 
    birth_date = datetime(year,month,day)
    date_to_50 = birth_date + timedelta(days=(50*365))
    remaining_datetime = relativedelta.relativedelta(date_to_50, today)

    # making string with years, months, and days
    remaining_datetime = "{0} years, {1} months, {2} days".format(remaining_datetime.years,
             remaining_datetime.months, remaining_datetime.days)
    
   
    return remaining_datetime


