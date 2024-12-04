def ask_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number!")


def ask_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number!")
