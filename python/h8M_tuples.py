# **********cannot change*********
# Cannot update the value
# no squ brakets[]

# same as list but they are immutable
t = (99, 98, 66, 67, 69, 66)
no = 99, 98, 66, 67, 69, 66, 567, 456, 3456  # this is also a tuple
t1=() #empty tuple
t2=(1) #wrong way to declare single element tuple
t3=(1,) #correct way

print(t)
print(no)
print(t1)
print(t2)
print(t3)

print(t[0])  # Printing elements of tuple

#Methods
a=(1,7,2)
#COUNT...print how many times they appear
print(a.count(2))

# 2.Index...show index when they appear first
print(a.index(7))
