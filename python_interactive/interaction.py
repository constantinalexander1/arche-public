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
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()