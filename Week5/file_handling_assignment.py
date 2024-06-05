def create_file():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Hello, my name is Esther.\n")
            file.write("The second line includes a number: 12345\n")
            file.write("Here's the third line with some text.\n")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        with open('my_file.txt', 'r') as file:
            # Read and display the contents of the file
            content = file.read()
            print("File Contents:")
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

def append_file():
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending the fourth line.\n")
            file.write("Appending the fifth line with number: 67890\n")
            file.write("Finally, the sixth line.\n")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    create_file()
    read_file()
    append_file()
    read_file()  # Read again to show updated content

if __name__ == "__main__":
    main()
