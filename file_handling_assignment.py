# file_handling_assignment.py

try:
    # Step 1: Write to the file (initial content)
    with open('my_file.txt', 'w') as file:
        file.write("Line 1: This is the first line.\n")
        file.write("Line 2: The number is 42.\n")
        file.write("Line 3: Python is great for file handling!\n")
    print("Initial content written to 'my_file.txt'.\n")

    # Step 2: Append additional lines to the file
    with open('my_file.txt', 'a') as file:
        file.write("Line 4: This line is appended to the file.\n")
        file.write("Line 5: Appending more data is easy!\n")
        file.write("Line 6: Final appended line.\n")
    print("Additional content appended to 'my_file.txt'.\n")

    # Step 3: Read and display the updated content
    with open('my_file.txt', 'r') as file:
        content = file.read()

    # Display the updated file content on the console
    print("Updated content of 'my_file.txt':")
    print(content)

# Catch specific exceptions
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: Permission denied when trying to access 'my_file.txt'.")
except Exception as e:
    # Catch any other exceptions
    print(f"An unexpected error occurred: {e}")

finally:
    print("\nFile handling operation completed.")
