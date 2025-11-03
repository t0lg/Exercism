def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400, so it's a leap year
            else:
                return False  # Divisible by 100 but not by 400, so not a leap year
        else:
            return True  # Divisible by 4 but not by 100, so it's a leap year
    return False  # Not divisible by 4, so not a leap year


#def leap_year(year):return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)#