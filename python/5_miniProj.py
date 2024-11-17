firstNo=input("Enter first no :")
SecondNo=input("Enter Second no :")
operator=input("enter the operator :")
# type casting
# firstNo=int(firstNo)
if (operator=='+'):
    print(int(firstNo) + int(SecondNo))
elif (operator=='-'):
    print(int(firstNo) - int(SecondNo))
elif (operator=='*'):
    print(int(firstNo) * int(SecondNo))
elif (operator=='/'):
    print(int(firstNo) / int(SecondNo))
elif (operator=='%'):
    print(int(firstNo) % int(SecondNo))
else:
    print("enter valid operator")
    