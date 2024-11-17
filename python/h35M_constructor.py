class Employee:
    company="Google"

    def __init__(self,name,salary): # constructor
        print("Employee is created!")
        self.name=name
        self.salary=salary

    def getdetails(self):
        print(f"Name : {self.name}")
        print(f"salary : {self.salary}")
        

ronak=Employee("Ronak",100000) # parameters are must.
#automatically init is called
ronak.getdetails()