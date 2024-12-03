import random

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
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve",
             "Frank", "Grace", "Hannah", "Ivan", "Jasmine",
             "Kevin", "Luna", "Mona", "Nathan", "Olivia",
             "Paul", "Quinn", "Rachel", "Sam", "Tina",
             "Ursula", "Victor", "Wendy", "Xander", "Yara",
             "Zane"]
    jobs = ["Engineer", "Designer", "Teacher", "Doctor", "Developer",
            "Artist", "Nurse", "Chef", "Photographer", "Lawyer",
            "Pilot", "Scientist", "Writer", "Architect", "Dentist",
            "Mechanic", "Farmer", "Electrician", "Plumber", "Translator",
            "Veterinarian", "Carpenter", "Journalist", "Accountant", "Actor"]

    data = []
    for i in range(count):
        # names[random.randint(0, len(names)-1)] --> random.choice(names)
        data.append([random.choice(names), random.randint(1, 100), random.choice(jobs)])
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
