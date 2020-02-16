
# Ques 2:
# Write a main.py file that import these functions and show the use of them.

from my_date import date_op

birth_date = input("Enter birth date (yyyy/mm/dd) : ")

birth_date = "".join(char if char.isdigit()
                     else " " for char in birth_date).split()

year = int(birth_date[0])
month = int(birth_date[1])
day = int(birth_date[2])

if not date_op.check_date(year, month, day):
    print("Invalid date!!!")
    exit()

print("Today is ", date_op.get_current_datetime())

age = date_op.get_age(year, month, day)

print("Age is ", age)

print("Date of birth is ", date_op.birth_date(age))

print("Time until 50 is ", date_op.time_to_50(year, month, day))
