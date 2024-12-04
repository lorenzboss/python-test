import re


def check_format(input_string):
    pattern = r'^\d{2}\.\d{2}\.\d{2}$'
    return re.match(pattern, input_string)


def date_to_seconds(time):
    parts = time.split(".")
    return 3600 * int(parts[0]) + 60 * int(parts[1]) + 1 * int(parts[2])


def start():
    time = input("Enter current time: ")

    if check_format(time):
        seconds = date_to_seconds(time)
        print("Today you already lived:")
        print(f" - {seconds:9.2f} seconds!")
        print(f" - {seconds / 60:9.2f} minutes!")
        print(f" - {seconds / 3600:9.2f} hours!")
    else:
        print("Please enter a valid time!")


while True:
    start()
