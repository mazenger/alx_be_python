def perform_operation(num1: float, num2: float, operation: str):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num1 == 0:
            print("cant divide zero")
        else:
            return num1 / num2

print(perform_operation(0, 2, "divide"))