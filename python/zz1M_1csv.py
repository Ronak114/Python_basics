import csv

def create_csv_file(file_name):
    try:
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Age', 'City'])
            print(f'{file_name} created successfully.')
    except Exception as e:
        print(f'Error: {e}')

def write_to_csv(file_name, data):
    try:
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
            print('Data written to the CSV file successfully.')
    except Exception as e:
        print(f'Error: {e}')

def read_csv_file(file_name):
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except Exception as e:
        print(f'Error: {e}')

def main():
    file_name = input('Enter the name of the CSV file (e.g., data.csv): ')

    while True:
        print("\nMenu:")
        print("1. Create a CSV file")
        print("2. Write to the CSV file")
        print("3. Read the CSV file")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            create_csv_file(file_name)
        elif choice == '2':
            name = input('Enter name: ')
            age = input('Enter age: ')
            city = input('Enter city: ')
            data = [name, age, city]
            write_to_csv(file_name, data)
        elif choice == '3':
            read_csv_file(file_name)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
