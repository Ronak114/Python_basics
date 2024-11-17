#Best way to open and close file automatically.
# no need to close the file...it will done automatically
with open('another.txt','r') as f:
    a=f.read()
print(a)

with open('another2.txt','w') as f:
    a=f.write("Ronak")
print(a)