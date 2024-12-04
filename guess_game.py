import random


def ask_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number!")


def start_game():
    print("Guess the number between 1 and 100")
    number = random.randint(1, 100)
    attempts = 0
    while True:
        user_input = ask_int("Your guess: ")
        attempts += 1
        if user_input < number:
            print("Higher!")
        elif user_input > number:
            print("Lower!")
        else:
            print("Your guess ist correct!")
            print(f"It took you {attempts} attempts to guess the number.")
            break


start_game()