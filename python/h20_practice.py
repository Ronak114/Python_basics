# # print table using for loop.
# a = int(input("Enter the number : "))
# for i in range(1, 11):
#     print(str(a) + " X " + str(i) + " = " + str(a * i))
#     print(f"{a}X{i}={a*i}")  # f string
#     # Both line will be executed.
#     i += 1


# # Same que using while loop.
# a = int(input("Enter the number : "))
# i=1
# while (i<=10):
#     print(a*i)
#     i += 1


#WAP to greet all person starts with S.
# l1=["Ronak","Soham","Sachin","Rahul"]
# #own soln ..wrong one
# # for i in l1:
# #     for j in i:
# #         if(str(j(0))=='S'):
# #             print("hello")
# #         else:
# #             pass

# #RightOne.
# for name in l1:
#     if name.startswith('S'):
#         print("Hello " + name)


# #given no prime or not
# b=int(input("Enter the no. : "))
# prime=True
# for i in range(2,b):       
#     if (b%i==0):
#         prime=False
#         break
# if prime:
#     print("Prime No")
# else:
#     print("Not a Prime No.")


# #Sum of first n natural no using for loop.
# c=int(input("Enter the no. : "))
# sum=0
# for i in range(0,c+1):
#     sum += i
# print(sum)


#Sum of first n natural no using while loop.
c=int(input("Enter the no. : "))
i=1
sum=0
while (i<=c):
    sum += i
    i += 1
print(sum)