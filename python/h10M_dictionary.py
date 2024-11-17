dict = {
    "name": "by which ppl call you",
    1: 11,
    "marks": [1, 2, 3, 4],
    "anotherdict": {"Ronak": "player"},
}
print(dict[1])
print(dict["name"])
print(dict["marks"])
print(dict["anotherdict"])
print(dict["anotherdict"]["Ronak"])  # nested dict

# dictionary are changable
dict["name"] = "Ronak"
print(dict["name"])

# Methods of dictionary
print(dict.keys())  # prints all the keys in list formate
print(type(dict.keys()))  # o/p dict_keys
print("wertyuiop[]")
print(list(dict.keys()))  # op will be list :)

print(dict.values())  # print valuues
print(type(dict.values()))
print(list(dict.values()))

print(list(dict.items()))  # list of(key,value)

# to update the dictionary
print(dict)
updated = {
    "Teja": "friend",
    "Riya": "bff",
    1: 123,  # update the value of 1..will noy make new key.
}
dict.update(updated)
print(dict)
# print(dict.update{"Teja":"friend"})..will not work

# get method
print(dict.get("name"))
print(dict["name"])

print(dict.get("name1"))# op none
print(dict["name1"]) # will throw error(bcz key must present)