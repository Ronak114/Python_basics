#Creating a class and its objject.
class student:
  Id = 1
s1 = student()
print(s1.Id)

#Inheritance
class employee:
  def __init__(self, Id, name):
    self.ID = Id
    self.Name = name

  def printname(self):
    print(self.ID, self.Name)


x = employee("1", "Ronak")
x.printname()

