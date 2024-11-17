# if another.txt is not prsent it will create it. AND add that line to file
f=open('another.txt','w')
f.write("Add this line to text")
f.close()
# kuch changes kiye toh overlapp honga

 
#this block of code can run multiple times.
f=open('another.txt','a')
f.write(" I am appending") 
f.close()
#kuch changes kiye toh last mai add honga