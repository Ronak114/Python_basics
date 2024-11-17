a = "Ronak's"
d = 'Ronak"s'
c = """Ronak and it's"""
print(a, " ", d, " ", c)
print(a + d)  # concatenating two string
print(a[0])
# a[3]="e" #we cannot change string

# SLICING from start index till end index(end index is excluded)
print(a[0:3])

# slice from start.
b = "Hello, World!"
print(b[:5])

# slice to end
print(b[2:])  # end se 2 index tak print honga

# negative indexing
print(b[-5:-2])

# slicing with skip value
z="abcdefghijklm"
r = z[0::2]  # end codn not mentioned...skipping 1 value
print(r)

p="qwertyuiop"
print(p[1::3])

# Escape Sequence Characters
# \n \t \ \\
story = "Hello everyone my name is ronak pawar.\n Nice \t to meet you"
print(story)


# to remove whitespaces from beg to end
p = " Hello, World! "
print(p.strip())  # returns "Hello, World!"

# split strings into sub strings
r = "Hello, World!"
print(r.split(","))  # returns ['Hello', ' World!']
