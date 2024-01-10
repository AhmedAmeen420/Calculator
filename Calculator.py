def calculator():
    while True:
        print("Choose an operation:")
        print("- Division")
        print("- Multiplication")
        print("- Subtraction")
        print("- Addition")
        print("- Exit")

        operation = input("Enter your choice: ").lower()

        if operation == "exit":
            print("Exiting the calculator. Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "division":
            if num2 != 0:
                result = num1 / num2
                print("Result:", result)
            else:
                print("Cannot divide by zero")
        elif operation == "multiplication":
            result = num1 * num2
            print("Result:", result)
        elif operation == "subtraction":
            result = num1 - num2
            print("Result:", result)
        elif operation == "addition":
            result = num1 + num2
            print("Result:", result)
        else:
            print("Invalid operation")

# Run the calculator
calculator()
