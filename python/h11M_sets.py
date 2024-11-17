a = {1, 2, 2, 3, 4}
print(a)  # 2 will not be printed
print(type(a))  # op set

# empty set
#This will create empty dict not empty set
b = {}
print(type(b))  # op dictionary
 
c=set()
print(type(c)) # op set

#Mathods of sets
#To add in set
c.add(1)
c.add(77)
c.add(9)
c.add(77) # will not add..no duplicates
print(c)

#in sets we cannnot add list..bcz list are unhasable(we can change list but not set)....it will give error
# c.add([5,4,2,1]) 
# print(c)

#can add tuple..bcz they are hasable
c.add((4,5,6,7))
print(c)

#cannot add dict..bcz it is unhasable
# c.add({4:5})
# print(c)

#length..length of set
print(len(c))

#remove..remove item
# print(c.remove(9)) # op none
c.remove(9)
# c.remove(90) # throws erroe..bcz it is not present
print(c)

#pop..randomly ek element ko remove krdenga
print(c.pop()) # it will show that element
print(c) # yaha woh element print nhi honga

#clear..clears all
c.clear()
print(c)