# ##Python programme to check the no. of days in a month

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years"""

    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

def days_in_months(year, month):
    """Returns number of days in that month of that year"""

    if not 1 <= month <= 12:
        return 'Invalid Month!'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

if __name__ == '__main__':
    year = int(input('Enter the year: '))
    month = int(input('Enter the month number: Ex. January - 1: '))
    
    result = days_in_months(year, month)
    print(f"Number of days: {result}")