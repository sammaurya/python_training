

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


def is_leap_year(year):
    if((year % 4 == 0) and (year % 100 != 0) or year % 400 == 0):
        return True
    return False


def is_valid_date(year, month, day):
  
    try:
        birth_date = datetime(year, month, day)
        if birth_date > datetime.today():
            raise Exception
        
    except:
        return False
    else:
        return True

def get_current_datetime():
    return datetime.today()


def birth_date(age):
    today = get_current_datetime().date()
    # extracting years, months and days from the age string
    age = "".join(char if char.isdigit() else " " for char in age).split()
    years = today.year - int(age[0])
    months = int(age[1])
    days = int(age[2])

    if months > today.month:
        months = (today.month + 12) - months
        years -= 1
    elif months < today.month:
        months = today.month - months

    if months == 3 and today.day < days:
        days -= 2

    birth_date = datetime(years, months, today.day)
    birth_date = birth_date - timedelta(days=days)

    # formating birth_date in string
    birth_date = "{0}-{1}-{2}".format(birth_date.year,
                                      birth_date.month, birth_date.day)

    return birth_date


def get_age(year, month, day):
    # get current date and time
    today = get_current_datetime().date()

    # birth year, month, day to datetime class
    birth_date = datetime(year, month, day)

    # calculating relative difference between current date and birth date
    age = relativedelta.relativedelta(today, birth_date)

    # making string with years, months, and days
    age_str = "{0} years, {1} months, {2} days".format(
        age.years, age.months, age.days)

    # returning string
    return age_str


def time_to_turn_50(year, month, day):
    today = get_current_datetime().date()
    if month == 2 and day == 29:
        day = 28

    date_to_50 = datetime(year+50, month, day)
    time_to_50 = relativedelta.relativedelta(date_to_50, today)
    years = time_to_50.years
    months = time_to_50.months
    days = time_to_50.days
    # making string with years, months, and days
    time_to_50 = "{0} years, {1} months, {2} days".format(
        years, months, days)
    return time_to_50
