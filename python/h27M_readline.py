f=open('another1.txt')
data=f.readline() # Reads 1st line even with \n
print(data)
data=f.readline() # Reads 2nd line
print(data)
data=f.readline() # Reads 3rd line
print(data)
data=f.readline() # Reads 4th line
print(data)
f.close()
 