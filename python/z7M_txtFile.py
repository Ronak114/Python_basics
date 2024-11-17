import fileinput
# This will create a text file and add that content to it.
file = open('Roo.txt','w')
fileinput.input()
file.write("Hello Ronak!!")
file.write("Happy Birthday!!")
file.close()

# To illustrate append() mode
file = open('Ronak.txt', 'a')
file.write("It's Sept 14 ,Ur Birthday!!")
file.write(input('Enter ur msg'))
file.close()

#for reading into a file
file=open("Ronak.txt","r")
print(file.read())
file.close()