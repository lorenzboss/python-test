from tabulate import tabulate


def get_user_input():
    while True:
        try:
            count = int(input("How many people should be displayed in the table?: "))
            if count > 0:
                return count
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def generate_data(count):
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    jobs = ["Engineer", "Designer", "Teacher", "Doctor", "Developer"]
    ages = [24, 30, 28, 35, 27]

    # Generate data based on the requested count
    data = []
    for i in range(count):
        index = i % len(names)  # Cyclically repeat the data
        data.append([names[index], ages[index], jobs[index]])
    return data


def display_table(data):
    headers = ["Name", "Age", "Job"]
    print(tabulate(data, headers, tablefmt="fancy_grid"))


def start_game():
    person_count = get_user_input()
    data = generate_data(person_count)
    display_table(data)


start_game()
