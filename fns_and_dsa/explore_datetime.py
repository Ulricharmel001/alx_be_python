import datetime
from datetime import datetime
from datetime import timedelta



""""
understanding datetime module in python
Creating Function to print out current date and time
create a function name "display_current_datetime"
past a parameter known as current_date
create a variable called "current_datetime"
and return the current date and time

"""

def display_current_datetime(current_date):
    from datetime import datetime
    current_date  = datetime.now() # current date and time == datetime.now(), this line of code display current date and time and store in a variable called current_date
    return current_date

display_current_datetime("friday") # call the function
print(display_current_datetime("friday")) # print the current time and date


""""
Function to calculate future_date


"""




from datetime import datetime, timedelta

def calculate_future_date(number_of_days):
    today = datetime.today()
    future_date = today + timedelta(days=number_of_days)
    return future_date

# Get input from user outside the function
try:
    days = int(input("Enter the number of days to add: "))
    future = calculate_future_date(days)
    print("Future:", future.strftime("%Y-%m-%d"))
except ValueError:
    print("Invalid input. Please enter a valid number.")






















