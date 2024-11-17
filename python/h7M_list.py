# *************can change*********
# Creating a list usin[] with diff datatypes
marks = [99, 97, 57, "maths"]

# print all the elements
print(marks)

# Access using index
print(marks[0])  # 0-based indexing
print(marks[-1])  # indexing from end

# List Slicing..Same as string(SEE THE FUNCTIONS OF STRING)
print(marks[0:2])  # o/p 99,97

# change value of list
marks[0] = 56
print(marks)

# functions on list.
l1 = [1, 8, 2, 5, 4, 6, 11]

# To sort the items
l1.sort()  # original l1 is sorted
print(l1)

# To reverse the list
l1.reverse()
print(l1)

# to add new item in last position.
l1.append(66)
print(l1)

# to add new item at any position.
l1.insert(2, "klaus")  # 2 is index
print(l1)

# to remove any item from given index
l1.pop(2)
print(l1)

# to remove any item
l1.remove(66)
print(l1)


# to check any item exist or not...boolean output.
print(1 in l1)
print("5" in l1)  # 5 considered as string

# length of list
print(len(l1))  # counting start from 1.

# to clear the whole list
l1.clear()
print(l1)
