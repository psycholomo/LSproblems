def is_leap_year(num):
    if year < 1752 and year % 4 == 0:
        return True
    elif num % 400 == 0:
        return True
    elif num %100 == 0:
        return False
    else:
        return num % 4 == 0