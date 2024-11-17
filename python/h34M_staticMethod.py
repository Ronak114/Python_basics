class Employee:
    @staticmethod
    def greet():
        print("Good Morning Ronak")


ronak = Employee()
ronak.greet()  # Employee.greet() #As staticmethod is used...No need to use self.
ronak.greet()  # Employee.greet(ronak) #when staticmethod was not used...need to use self.x
