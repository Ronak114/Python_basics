# # Read text from file poems.txt and find whether it contain twinkle or not.
# f=open('poems.txt','r')
# t=f.read()
# if 'twinkle' in t:
#     print("twinkle is present")
# else:
#     print("Twinkle is not present")
# f.close()


# #Own ans
# def game():
#     return 89
# score=game()
# f=open('Hi_score.txt','r')
# t_Str=f.read()
# if (t_Str==" "):
#     f=open("Hi_score.txt","w")
#     f.write(str(score))
#     f.close()
# elif int(t_Str) < score: #doubt aata hai
#     f=open("Hi_score.txt","w")
#     f.write(str(score))
#     f.close()
# f.close()


# #harry bhaiyaa
# def game():
#     return 89
# score=game()
# with open('Hi_score.txt') as f:
#     hiscore=int(f.read())
# if (hiscore<score) :
#     with open("Hi_score.txt","w") as f:
#         f.write(str(score))


# #multiplication table in multiple file and same folder.
# for i in range (2,21):
#     with open(f"tables/Multiplication_table_of_{i}.txt","w") as f:
#         for j in range (1,11):
#             f.write(f"{i}X{j}={i*j}\n")


# #replace a word from a file
# with open("another1.txt") as f:
#     data=f.read()

# data=data.replace("Ronak","Roo")
# with open("another1.txt","w") as f:
#     f.write(data)


# #Same qur for list
# list=["A","B","C","D","E","F","G","H"]
# with open("another3.txt") as f:
#     data=f.read().lower() # it will check for lower case too

# for l in list:
#     data=data.replace(l,"!@#")

#     with open("another3.txt","w") as f:
#         f.write(data)


# #NO.of line
# content=True
# i=1
# with open("another3.txt") as f:
#     while content:
#         content=f.readline()
#         if 'you' in content.lower():
#             print(content)
#             print("Yes present")
#             print(i)
#         i+=1


# #copy a text file
# with open("another1.txt") as f:
#     data=f.read()
# with open("copy.txt","w") as f:
#     f.write(data)


# # find whether a file matches the other file or not.
# file1="another1.txt"
# file2="copy.txt"
# with open(file1) as f:
#     f1=f.read()
# with open(file2) as f:
#     f2=f.read()
# if f1==f2:
#     print("Same Same")
# else:
#     print("Not Same")


# #Wipe out contrnt of a file.
# filename="copy.txt"
# with open(filename,"w") as f:
#     f.write("")


#rename a file..Create new one same with diff name,copy content,delete pre one.
import os
oldName="copy1.txt"
newName="renamed_by_python.txt"
with open(oldName) as f:
    data=f.read()
with open(newName,"w") as f:
    f.write(data)
os.remove(oldName)