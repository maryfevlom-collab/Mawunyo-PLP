# Simple Calculator Program
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == '+':
    result = first_number + second_number  
    print(f"The result of {first_number} + {second_number} is: {result}")
elif operation == '-':
    result = first_number - second_number
    print(f"The result of {first_number} - {second_number} is: {result}")
elif operation == '*':
    result = first_number * second_number
    print(f"The result of {first_number} * {second_number} is: {result}")
elif operation == '/':
    if second_number != 0:
        result = first_number / second_number
        print(f"The result of {first_number} / {second_number} is: {result}")
    else:
        result = "Error: Division by zero is not allowed."
        print(result)
else:
    result = "Error: Invalid operation."
    print(result)