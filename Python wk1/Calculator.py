# Calculator Program

def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero!"
        result = num1 / num2
    else:
        return "Error: Invalid operation!"

    return f"{num1} {operation} {num2} = {result}"

# Example usage:
print(calculator())
