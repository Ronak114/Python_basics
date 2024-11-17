#jtaking inputs
# firstNo=input("enter 1st no :")
# secondNo=input("Enter 2nd no :")
# sum=int(firstNo) + int(secondNo)
# print(sum)

# for loop
for i in range(5):
    print(i)
#starts from 0 and 5 is not included.

for i in range(9,11):
    print(i)

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1

#list
marks = [99, 97, 57, "maths"]
print(marks)
print(marks[0:2])


#for loop in list
names=["Lee","Alexx","lenaa","Anna","Maddy"]
for i in names:
    print(i)

#functions
#to add new item in last position.
names.append("Damonn")
print(names)
#to insert new item at any position.
names.insert(2,"klaus") # 2 is index..0 based indexing
print(names)
#to check any item exist or not...boolean output.
print("Lee" in names)
print("lee" in names)
#length of list
print(len(names))#counting start from 1.


#to clear the whole list
names.clear()
print(names)

#fun