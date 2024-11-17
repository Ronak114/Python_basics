
#***********indentation is imp*********
#if-elif ladder
#Even if both codn are true ,we will be like first come first serve..ek baar execute hoke ladder se bahar
b=45
if(b>3):
    print("no. greater than 3")
elif(b>7):
    print("no. greater than 7")
else:
    print("No greater than 3 and 7")


#Multiple if statements.
#if are independent statements..every condn will be checked.
c=45
if(c>3):
    print("no. greater than 3")
if(c>7):
    print("no. greater than 7")

if(c>10):
    print("no.id greater than 10")
else:
    print("No greater than 3 and 7")

#Q0
age=int(input("enter age:"))
if age>=18:
    print("Can vote")
elif (age<18 and age>3):
    print("Kid broo")
else:
    print("no") 

    
print("thank you")#outide the condn statement