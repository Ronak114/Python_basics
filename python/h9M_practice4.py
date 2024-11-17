# WAP to store seven fruits in list entered by user.
# f1=input("Enter fruit 1:")
# f2=input("Enter fruit 2:")
# f3=input("Enter fruit 3:")
# f4=input("Enter fruit 4:")
# f5=input("Enter fruit 5:")
# f6=input("Enter fruit 6:")
# f7=input("Enter fruit 7:")
# fruits=[f1,f2,f3,f4,f5,f6,f7]
# print(fruits)

# # WAP to accept marks of 6 students and display them in sorted manner
# m1 = int(input("Enter marks of student1:"))
# m2 = int(input("Enter marks of student2:"))
# m3 = int(input("Enter marks of student3:"))
# m4 = int(input("Enter marks of student4:"))
# m5 = int(input("Enter marks of student5:"))
# m6 = int(input("Enter marks of student6:"))
# # input will be in string formate
# marks = [m1, m2, m3, m4, m5, m6]
# marks.sort()
# print(marks)
# # print(marks.sort()) # this will not work

#check that tuple cannot be changed
a=(2,6,3,5,1,9)
# a[0]=8 #...gives error
print(a)

#to sum a list of 4 no.s
b=[2,3,4,5]
print(b[0]+b[1]+b[2]+b[3])
print(sum(b))

#Count 0 in tuple
c=(7,0,8,0,0,9)
print(c.count(0))
