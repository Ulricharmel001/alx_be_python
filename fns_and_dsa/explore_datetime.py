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
    return formatted_date

# Part 2: Calculate future date
def calculate_future_date(number_of_days):
    today = datetime.today()
    future_date = today + timedelta(days=number_of_days)
    return future_date

# Main Program Execution
if __name__ == "__main__":
    # Display current datetime
    display_current_datetime()

    # Prompt user for input and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future = calculate_future_date(days)
        print("Future date:", future.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")




















