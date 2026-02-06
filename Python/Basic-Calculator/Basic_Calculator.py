def save_history(history):
    with open("calculator_history.txt", "a") as file:
        file.write(history)

def show_history():
    try:
        with open("calculator_history.txt", "r") as file:
            history = file.read()
            if history:
                print("\nCalculation History:")
                print(history.strip())
            else:
                print("\nNo calculation history found.")
    except FileNotFoundError:
        print("\nNo calculation history found.")

def create_session():
    with open("calculator_history.txt", "a") as file:
        file.write("=== New Session Started ===\n")

def clear_history():
    with open("calculator_history.txt", "w") as file:
        file.write("")
    print("Calculation history cleared.")

def main():
    print("Welcome to the Python Calculator!")
    create_session()

    calculation_number = 1

    while True:
        print("\nSelect an operation:")
        print("00. Simple Calculator")
        print("0. Exit")
        print("1. Clear History")
        print("2. Show History")
        print("3. Create new session")

        choice = input("Enter your choice (0, 1, 2, enter anything): ")

        if choice == '0':
            print("Thank you for using the calculator. Goodbye!")
            break
        elif choice == '1':
            clear_history()
            continue
        elif choice == '2':
            show_history()
            continue
        elif choice == '3':
            create_session()
            print("New session created.")
            continue

        num1 = input("Enter the first number: ")
        try:
            num1 = float(num1)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        operator = input("Enter the operator (+, -, *, /): ")
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator. Please try again.")
            continue

        num2 = input("Enter the second number: ")
        try:
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                continue
        else:
            print("Invalid operator. Please try again.")
            continue

        print(f"The result of {num1} {operator} {num2} is: {result}")

        save_history(f"Calculation Number '{calculation_number}' => {str(num1)} {operator} {str(num2)} = {str(result)}\n")

        calculation_number += 1

if __name__ == "__main__":
    main()