
"""
Creating a function to carryout basic maths operations
parameters are "num1, num2 and operations"
operation is done between num1 and num2
value stored in a variable called result
and the return value is the result of the operation
division by 0 is not allowed
if someone tries to divide by 0, it would display an "Error: cannot divide by 0"

"""
def perform_operation(num1, num2, operation): # function to carry out math operations
    if operation == "add":
        result = num1 + num2
        return result # return value
    elif operation == "subtract":
        result = num1 - num2
        return result
    elif operation == "multiply":
        result = num1 * num2
        return result
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero" # division by 0 is not possible
        else:
            result = num1 / num2
            return result






