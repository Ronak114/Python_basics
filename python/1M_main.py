#basics
print("hello Ro..let's begin :)")
print("Python is case sensitive language")
print(5+8)

#variables
name="Ronak" #String
age=21 #int
print(name,age) #this is also valid ...experiment by me.
print(age )
#variables are changeable.
name="Ro"
print(name)

#types of variable.(Data-types)
# 1.String 2.Integer-int,-float,-boolean 
price=20.00 #float
is_adult=True #true not work...sensitive
#adv..no need to specify type before we define

#exercise
firstName="Tony"
lastName="Stark"
age=51
isGenius=True
print (firstName)
print (lastName)
print (age)
# **************imp***************
print ("Tony is Genius " + str(isGenius)) #doubtttttttt..cleared

#input
naav=input("What is your name?")
print(naav)
print("hello " + naav) #concatenation

#exercise
print("Tell me your superhero name ?")
superhero=input()
print(superhero)

#type conversion...Y needed (inputs alys takes in string format)
oldAge=input("Enter your old age:")
#string cannot add in int
#whatever age we will provide it will take it in str formate like "oldAge".
#here comes the role of type conversion.
currAge=int(oldAge) + 2 
print(currAge)
#int() float() str() bool()

