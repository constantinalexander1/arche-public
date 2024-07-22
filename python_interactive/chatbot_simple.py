import random

from word_bank import verben, nomen, adjektive

## Interesting string methods:
# https://www.w3schools.com/python/python_ref_string.asp

# Lowercase string: string.lower()
# Returns true if the string ends with the specified value: string.endswith()
# Splits the string at the specified separator, and returns a list: split()
# Capitalizes the first character of a string: string.capitalize()

## Interesting random methods:
# Random integer between a and b: random.randint(a, b)
# Random choice from a list: random.choice(list)


def main():
    while True:
        # Prompt the user for input
        command = input("Enter a command: ")

        # Process the command
        if command == "quit":
            print("Exiting...")
            break
        if command.startswith("My name is:"):
            name = command[11:].strip()
            print(f"Hello, {name}!")
        if command.startswith("Roll a dice"):
            number = random.randint(1, 6)
            print(f"The dice shows {number}")
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()