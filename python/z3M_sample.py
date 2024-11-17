# Table of 2 to 11
for i in range(2, 11):
    print("table of:" + str(i))
    for j in range(1, 11):
        print(i * j)

# Finding min and max among three no.
num1 = int(input("Enter First number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter Third number:"))
max_min = [num1, num2, num3]
print("Max No:", max(max_min))
print("Min No:", min(max_min))


# Average of user given array
n = int(input("Enter the number of elements: "))
user_array = []

for i in range(n):
    num = float(input("Enter element: "))
    user_array.append(num)

total = 0
for num in user_array:
    total += num

print("The average of the elements is:", total / n)

# Using all data types and performing valid operations.
a = int(9)
is_adult = True

# to show type of data type
print(type(a))
print(type(is_adult))

# operations on string
Name = "Ronak"
LastNAme = "Pawar"
print(type(Name))
print(len("Name"))
print(Name[0:3])
print(Name[-5:-2])
print(Name + LastNAme)

# operations on list
list = [99, 97, 57, "maths"]
print(type(list))
# list.sort()  # sort
list.reverse()  # reverse
list.append(66)  # to add new item in last position.
list.insert(2, "klaus")  # to add new item at position 2
print(list)

# operations on tuple
tuple = (99, 98, 66, 67, 69, 66, 99)
print(type(tuple))
print(tuple.count(99))  # count
print(tuple.index(99))  # Index

# operations on dict
dict = {"name": "Roo", 1: 11, "marks": [1, 2, 3, 4], "anotherdict": {"Ronak": "player"}}
print(type(dict))
print(dict.keys())  # print keys
print(dict.values())  # print valuues
print(dict.items())  # list of(key,value)

# operations on set
set = {1, 2, 2, 3, 4}
print(type(set))
set.add(77)
print(len(set))
set.remove(77)
print(set)
set.clear()
print(set)
