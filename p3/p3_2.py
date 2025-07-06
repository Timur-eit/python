import calendar

"""
Год високосный, если:
Делится на 4 и не делится на 100,
или делится на 400.
"""


def is_leap_year_elif(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def is_leap_year_one_line(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def is_leap_year_calendar(year: int) -> bool:
    return calendar.isleap(year)


year = int(input("Введите год: "))

print("Вариант с elif:", is_leap_year_elif(year))
print("Вариант в одну строку:", is_leap_year_calendar(year))
print("Вариант через calendar:", is_leap_year_calendar(year))
