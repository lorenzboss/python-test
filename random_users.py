import random

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
    headers = ["Name", "Age", "Job"]
    print(tabulate(data, headers, tablefmt="fancy_grid"))


def start_game():
    person_count = get_user_input()
    data = generate_data(person_count)
    display_table(data)


start_game()
