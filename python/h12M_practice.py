# create a dict of hin wrds with value as eng translation.
dict={
    "subh":"morning",
    "raat":"night",
    "duphar":"afternoon",
    "sham":"evening"
}
print("Options are ",dict.keys())
a=input("User enter the key(Hin word):")
# print("Meaning:",dict[a])  #this is also true but it will give us the error
print(dict.get(a)) # this will not throw any error.

# #input 8 no. and display unique no ones
# num1=int(input("Enter the num 1:"))
# num2=int(input("Enter the num 2:"))
# num3=int(input("Enter the num 3:"))
# num4=int(input("Enter the num 4:"))
# num5=int(input("Enter the num 5:"))
# num6=int(input("Enter the num 6:"))
# num7=int(input("Enter the num 7:"))
# num8=int(input("Enter the num 8:"))
# set={num1,num2,num3,num4,num5,num6,num7,num8}
# print(set)

#Can we have a set of 18(int) and 18(str) as val in it?
s={18,"18",18.1}
print(s)

#length?
s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s)) #op 2...bcz 20 and 20.0 are considered same
print(s) #20.0 is not printed

# #Type of S?
# s={}
# print(type(s)) #op dict

#create 4 frds with name and language.
dict={}
# value1=input("Enter your Roo:")
# value2=input("Enter your Teja:")
# value3=input("Enter your Ronak:")
# value4=input("Enter your Tejasvi:")

# dict["Roo"]=value1
# dict["Teja"]=value2
# dict["Ronak"]=value3
# dict["Tejasvi"]=value4

# #ek line mai kaam horaha
# dict["Roo"]=input("Enter your Roo:")
# dict["Teja"]=input("Enter your Teja:")
# dict["Ronak"]=input("Enter your Ronak:")
# dict["Tejasvi"]=input("Enter your Tejasvi:")

# print(dict)
# #for same key ..updated value will appear.