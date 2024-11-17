#Example of railway application.

class RailwayForm: # class
    formType="Railwayform"
    def printData(self):
        print(f"Name:{self.name}")
        print(f"Train:{self.train}")

RonakAppln=RailwayForm() # object
RonakAppln.name="Ronak"
RonakAppln.train="Hum safar"

RonakAppln.printData()


#example of employee
class Employee: # class
    company="Google"
    salary=100

Ronak=Employee() # object
Teja=Employee() # object

print(Ronak.company) # O/P Google
print(Teja.company) # O/P Google

Employee.company="Youtube" # we can change any attribute of a class by this way

print(Ronak.company)  # O/P Youtube
print(Teja.company) # O/P Youtube

print(Ronak.salary) # O/P 100
print(Teja.salary) # O/P 100

# Creating instance attribute salary for both obj
Ronak.salary=300  
Teja.salary=400
print(Ronak.salary) # O/P 300
print(Teja.salary) # O/P 400

print(Teja.address) # O/P error
# as address doesn't exist not as instance/class



