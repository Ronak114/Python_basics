# Function to create a new text file
def create_file(filename):
    try:
        with open(filename, 'w') as file:
            print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {str(e)}")

# Function to write data to a text file
def write_to_file(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(data + '\n')
            print("Data written to the file successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {str(e)}")

# Function to read and display the contents of a text file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Contents of '{filename}':")
            for line in file:
                print(line.strip())  # Remove newline characters for display
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Create a new text file")
        print("2. Write data to the text file")
        print("3. Read and display the contents of the text file")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            filename = input("Enter the name of the text file to create: ")
            create_file(filename)
        elif choice == "2":
            filename = input("Enter the name of the text file to write to: ")
            data = input("Enter the data to write to the file: ")
            write_to_file(filename, data)
        elif choice == "3":
            filename = input("Enter the name of the text file to read: ")
            read_file(filename)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")
