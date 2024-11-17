# for loop in list
names = ["Lee", "Alexx", "lenaa", "Anna", "Maddy"]
for i in names:
    print(i)

# break and contiue
students = ["roo", "teja", "riya", "rachita", "Maya"]

for i in students:
    if i == "riya":
        break  # iske baad kuch execute in honga
    print(i)


for j in students:
    if j == "rachita":
        continue  # bass woh wle condn execute nhi hongi
    print(j)
