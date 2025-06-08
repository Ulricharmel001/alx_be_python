import datetime
from datetime import datetime
from datetime import timedelta

#
#
# """"
# understanding datetime module in python
# Creating Function to print out current date and time
# create a function name "display_current_datetime"
# past a parameter known as current_date
# create a variable called "current_datetime"
# and return the current date and time
#
# """""

from datetime import datetime, timedelta

# Part 1: Display current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate future date (user input and calculation inside)
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    today = datetime.today()
    future_date = today + timedelta(days= number_of_days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)
    return future_date

# Run the script only when executed directly
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()





















