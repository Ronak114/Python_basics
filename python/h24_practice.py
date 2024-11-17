# function to find greatest of 3 no.
# Own..worked
# def greatestNo(a,b,c):
#     return max(a,b,c)
# print(greatestNo(3,4,6))
# print(max(6,4,3)) #ye bhi directly kr skte.

# #harry bhaiya
# def greatestNo(a,b,c):
#     if(a>b):
#         if(a>c):
#             return a
#         else:
#             return c
#     else:
#         if(b>c):
#             return b
#         else:
#             return c
# print(greatestNo(7,4,9))


# #Covert Celsius to Fahr.
# def converter(c):
#     f=32+(c*(9/5))
#     return f
# print(converter(0))


# # stop adding next line by print function
# print("Ronak", end=" ")  # /n will be earesed
# print("Roo", end=" ")
# print("Riyaa", end=" ")
# print("Rahii", end=" ")


# #sum of first n no.
# def sum(a):
#     if a==0:
#         return 0 
#     return a+sum(a-1)
# print(sum(5))

# # Printing patterns
# # ***
# # **
# # *
# n=6
# for i in range(n):
#     print("*" * (n-i))


# #remove a given word from String and strip it at the same time.
# def removeStrip(string,word):
#     newStr=string.replace(word,"")
#     return newStr.strip()

# intro="      Ronak Dipak Pawar     "
# n=removeStrip(intro,"Ronak")
# print(n)


# # print multiplication table
# def table(n):
#     for i in range(1,11):
#         print(n*i)
# print(table(7))