def ask_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number!")


def ask_operator(a, b, message):
    while True:
        user_input = (input("+, -, *, / or e to exit: "))
        if user_input == "+":
            return print(f"The result ist: {a + b}")
        elif user_input == "-":
            return print(f"The result ist: {a - b}")
        elif user_input == "*":
            return print(f"The result ist: {a * b}")
        elif user_input == "/":
            return print(f"The result ist: {a / b}")
        elif user_input == "e":
            print("Good Bye...")
            exit()
        else:
            print("Please enter a valid statement!")


def start_game():
    while True:
        first_number = ask_float("Enter first number: ")
        second_number = ask_float("Enter second number: ")
        ask_operator(first_number, second_number, "+, -, *, / or e to exit: ")


start_game()