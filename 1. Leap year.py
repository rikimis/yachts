# 1. Leap year

def leap_year(year):
    year = int(year)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

print(leap_year(2000)) # = True
