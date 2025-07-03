def is_leap(year):
    if not (1900 <= year <= 10**5):
        raise ValueError("year must be between 1900 and 10^5")
    if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
        leap = True
    else:
        leap = False
    
    return leap

year = int(input())
