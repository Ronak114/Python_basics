 # self is a parameter which is automatically passed when obj is called.
#USE : can use class attribute + instance attribute.

class Employee:
    company="google"
    def getSalary(self):
        print("Salary is 100k")

ronak=Employee() # here new obj is created
ronak.getSalary()
# Employee.getSalary(ronak) # internally the abv line convert into this line.

# therefore,when self is not passes they consider as no paramter was their in class and how it came in obj..therefore we need to add self their.



class Employee:
    company="google"
    def getSalary(self):
        print(f"Salary:{self.salary} and company:{self.company}")

ronak=Employee()
ronak.salary=100000000
ronak.getSalary()