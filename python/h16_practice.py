# #find greatest of 4 no.
# num1=int(input("Enter the no1:"))
# num2=int(input("Enter the no2:"))
# num3=int(input("Enter the no3:"))
# num4=int(input("Enter the no4:"))
# #Ek line mai laam hua vroo
# # print(max(num1,num2,num3,num4))
# #by using if else.
# if(num1>num4):
#     f1=num1
# else:
#     f1=num4

# if(num2>num3):
#     f2=num2
# else:
#     f2=num3

# if(f1>f2):
#     print(f1)
# else:
#     print(f2)


# #To check student is pass or fail
# m1=int(input("enter marks sub1:"))
# m2=int(input("enter marks sub2:"))
# m3=int(input("enter marks sub3:"))
# total=(m1+m2+m3)/3
# if(m1<33 or m2<33 or m3<33):
#     print("fail")

# if(total<40):
#     print("fail")
# else:
#     print("pass")


# #It is Spam or not
# text=input("Enter the text:")

# if("make money" in text):
#     spam=True
# elif("buy no" in text):
#     spam=True
# elif("suscribe this" in text):
#     spam=True
# elif("click this" in text):
#     spam=True
# else:
#     spam=False

# if(spam):
#     print("This is a spam")
# else:
#     print("Not a spam")


# #Check username contain 10 char or not.
# username=input("Enter the user name:")
# if(len(username)<=10):
#     print("yess")
# else:
#     print("nooo")


#check item is present in list or not
name=["roo","teja","mrunal","shruti","sharvari","shraddha","duggu","vaish"]
item=input("enter the item to find:")
if item in name:
    print("true")
else:
    print("False")