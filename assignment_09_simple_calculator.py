def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return round(x / y, 2)


def modulus(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x % y


def exponent(x, y):
    return x ** y


def main():
    while True:
        print("\n============================")
        print("       SIMPLE CALCULATOR     ")
        print("============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")

        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                x = float(input("Enter first number : "))
                y = float(input("Enter second number: "))
            except ValueError:
                print("Error: Please enter valid numbers.")
                continue

            if choice == "1":
                result = add(x, y)
                print(f"Result: {x} + {y} = {result}")
            elif choice == "2":
                result = subtract(x, y)
                print(f"Result: {x} - {y} = {result}")
            elif choice == "3":
                result = multiply(x, y)
                print(f"Result: {x} * {y} = {result}")
            elif choice == "4":
                result = divide(x, y)
                print(f"Result: {x} / {y} = {result}")
            elif choice == "5":
                result = modulus(x, y)
                print(f"Result: {x} % {y} = {result}")
            elif choice == "6":
                result = exponent(x, y)
                print(f"Result: {x} ** {y} = {result}")
        else:
            print("Error: Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    main()
