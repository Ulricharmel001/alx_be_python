# import sys


# def safe_divide(self, numerator, denominator):
#     result = self.numerator / self.denominator
#     try:
#         self.numerator / self.denominator

#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#         sys.exit(3)
#     else:
#         print("Cannot divide by non-integer value")
#         sys.exit(2)
#     return result

# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float for division
        num = float(numerator)
        denom = float(denominator)

        # Check if denominator is zero
        if denom == 0:
            return "Error: Cannot divide by zero."

        result = num / denom
        return (f"The result of the division is {result}")

    except ValueError:
        return f"Error: Please enter numeric values only."



