   
# Pattern Generator and Number Analyzer

print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    # Display the menu
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    # Get the user's choice
    choice = input("Enter your choice: ")

    # Option 1: Generate a star pattern
    if choice == "1":
        rows = int(
            input("Enter the number of rows for the pattern: ")
        )

        for i in range(1, rows + 1):
            print("*" * (i + 1))

    # Option 2: Analyze a range of numbers
    elif choice == "2":
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        total = 0

        for number in range(start, end + 1):
            # Check whether the number is even or odd
            if number % 2 == 0:
                print(f"Number {number} is Even")
            else:
                print(f"Number {number} is Odd")

            # Add the current number to the total
            total += number

        # Display the sum
        print(
            f"Sum of all numbers from {start} to {end} is: {total}"
        )

    # Option 3: Exit the program
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    # Handle an invalid menu choice
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
