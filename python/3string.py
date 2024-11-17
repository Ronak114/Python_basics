name = "ronak Pawar"

# String functions

# length funtn
print(len(name)) #counts space

# ends with "anyStringName"
print(name.endswith("awar"))
print(name.endswith("awtyuar"))

# counting character
print(name.count("a"))  # can work for word too

# capitalize
print(name.capitalize())  # only r ko capital krenga

# Upper case
print(name.upper())
# actually it make a new string..no disturbance to original
print(name)

# Lower Case
print(name.lower())

# Find
print(name.find("ron"))
# o/p index...(-1=not found)
# 0 based indexing,Can find word too,only the first word can be shown

# replace
print(name.replace("Pawar", "Ironman"))
# this will not change original string,replace every occurance

# keyword
# when we just want to check the letter exist or not
print("R" in name)  # o/p True or False
print("R" not in name)  # o/p True or False..checking not

# Arithmetic Operators
# + - * / %
print("the sum of 3 and 4:", 3 + 4)
print(5**2)  # 5^2
print(5 // 2)  # it will divide and remove decimal part.

# Assignment Operator
# =,+=,-+..
# if evry line has new operation then it every tym var would be upgraded
# i=i+2    i+=2

# operator precedence.
# () * / + -

# Comparison Operator
# > < >= <= == !=  o/p boolean
print(5 < 2)

# Logical Operator
# or and not
print(2 > 3 or 2 > 1)
print(2 > 3 and 2 > 1)
print(not 2 > 3)
