"""Exercise 5: Days of the Month"""

# dictionary for the month numbers and number of days
days_in_month = {
    1: 31,  # January
    2: 28,  # February 
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# ask the user for the month number
month = int(input("Enter the month number between 1-12: "))

# then check if the input is valid
if month < 1 or month > 12:
    print("Invalid month number. Please enter a number between 1 and 12.")
else:
    # if the user selects February, ask if it's a leap year
    if month == 2:
        leap_year = input("Is it a leap year? (yes/no): ").lower()

        # adjust February for leap year
        if leap_year == "yes":
            print("February has 29 days in a leap year.")
        else:
            print(f"February has {days_in_month[month]} days.")
    else:
        # output the number of days for other months
        print(f"Month {month} has {days_in_month[month]} days.")
