from tabulate import tabulate


def get_user_input():
    """Asks the user how many people should be displayed in the table."""
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
    """Generates a list of sample data for the table."""
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
    """Displays the table in the console."""
    headers = ["Name", "Age", "Job"]
    print(tabulate(data, headers, tablefmt="fancy_grid"))


def main():
    """Main program."""
    person_count = get_user_input()
    data = generate_data(person_count)
    display_table(data)


if __name__ == "__main__":
    main()
