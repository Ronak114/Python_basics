import csv
#for creating a file and writing into a file
mydict = [{'Name': 'Ronak Pawar', 'Age': '20', 'Branch': 'IT'},
          {'Name': 'Tejasvi Urkande', 'Age': '23', 'Branch': 'CSE'},
          {'Name': 'Rahi Pawar', 'Age': '12', 'Branch': 'EXTC'}]
fields = ['Name', 'Age', 'Branch']
with open('csvFile.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(mydict)
#reading a csv file
with open('csvFile.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)