# Type casting
firstNo = input("enter 1st no :")
secondNo = input("Enter 2nd no :")
sum = int(firstNo) + int(secondNo)
# type conversion nhi liya toh woh concenate honge bcz input alys considered entered text as "string"
print(sum)
# print("the sum :" + sum)#errorr
# ***************imp**************
print("the sum :" + str(sum))
