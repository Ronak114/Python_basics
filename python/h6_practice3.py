# display GA with name using input()
greeting = "Good Afternoon "
name = input("Enter the name:")
print(greeting + name)

# fill the template
print("You already have entered name")
date = input("Now enter the date:")
letter = """Dear <|name|>,
           You are selected!
         <|date|>"""
letter = letter.replace("<|name|>", name)  # letter=letter..likhna is imp (remeber it)
letter = letter.replace("<|date|>", date)
print(letter)

# detect double spaces
school = "Alphonsa  sr.  sec    School  "  #  4ds convert to 2 ds.
print(school.find("  "))

# replace double spaces with
school = school.replace("  ", " ")
print(school)
