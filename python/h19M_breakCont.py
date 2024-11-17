# break
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("Done")
# ELSE part will not be executed bcz it got break


# Continue
# for i in range(10):
# *****aisa krenge toh skip nhi honga
# print(i)
# if(i==5):
#     continue

for j in range(10):
    if j == 5:
        continue
    print(j)


# pass statements.
p = 4
if p > 0:
    pass  # when we have to w8 for defining the defination
print("Roo")
