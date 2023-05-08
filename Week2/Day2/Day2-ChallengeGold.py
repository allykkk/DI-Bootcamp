from datetime import date, datetime


def calculate_age(date_str):
    birthdate = datetime.strptime(date_str, '%d/%m/%Y')
    today = date.today()
    is_plusone = (today.month, today.day) < (birthdate.month, birthdate.day)
    year_difference = today.year - birthdate.year
    age = year_difference - is_plusone
    return age


def make_cake(age):
    candle_num = age % 10
    is_even = (11 - candle_num) % 2
    if is_even == 0:
        print("       " + ((11 - candle_num) // 2) * "_" + "i" * candle_num + "_" * ((11 - candle_num) // 2))
    else:
        print("       " + ((11 - candle_num) // 2) * "_" + "i" * candle_num + "_" * ((11 - candle_num) // 2 + 1))
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")


def is_leap_year(date_str):
    birthdate = datetime.strptime(date_str, '%d/%m/%Y')
    if birthdate.year % 4 == 0 and (birthdate.year % 100 != 0 or birthdate.year % 400 == 0):
        return True
    else:
        return False


user_input = input("Please put date as DD/MM/YYYY: ")
age = calculate_age(user_input)
if is_leap_year(user_input):
    make_cake(age)
    make_cake(age)
else:
    make_cake(age)
