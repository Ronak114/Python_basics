# # Print Factorial using for loop
# a = int(input("Enter thr number: "))
# product = 1
# for i in range(1, a + 1):
#     product *= i
#     i += 1
# print(product)


# #Printing patterns.
# n=4
# for i in range(1,n+1):
#     print("*"*i)


#Print pattern.
''' 
  *
 ***
*****
'''

n=3
for i in range(3): # rows
    print(" " * (n-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (n-i-1))


# Table in reverse order.
