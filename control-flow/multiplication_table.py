# number = int(input("Enter a number to see its multiplication table:"))
# for numbers in [1,2,3,4,5,6,7,8,9,10]:
#     product = number * numbers
#     print(f"{number} * {s} = {product}")

number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
