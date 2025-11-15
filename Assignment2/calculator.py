"""
A basic calculator program that takes 2  numbers as input  and returns
the arithmetic values for addition, subtraction, and multiplication,
division, modulus, and exponential power. If 0 is used as the secondary
input it will print a message for division and modulus
"""

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

sum_result = first_number + second_number
difference_result = first_number - second_number
multiplication_result = first_number * second_number

if second_number != 0:
    division_result = first_number / second_number
    modulus_result = first_number % second_number
else:
    division_result = None
    modulus_result = None

power_result = first_number ** second_number

print(f"{first_number} + {second_number} = {sum_result}")
print(f"{first_number} - {second_number} = {difference_result}")
print(f"{first_number} * {second_number} = {multiplication_result}")

if division_result is not None:
    print(f"{first_number} / {second_number} = {division_result}")
else:
    print("Cannot divide by 0")

if modulus_result is not None:
    print(f"{first_number} % {second_number} = {modulus_result}")
else:
    print("Cannot perform modulus by 0")

print(f"{first_number} ** {second_number} = {power_result}")