# Use open funtn to read the content of a file
# f=open('another.txt','r')
f=open('another1.txt') # bydeafult mode is r
data=f.read() 
# data=f.read(5) # reads only firts 5 character
#read can done only once.

print(data)
f.close()