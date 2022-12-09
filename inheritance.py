# What is inherence?
# is the process where a class takes on the attributes and the methods of another class
# parent class gives the parameters to the child class 

# inherent, extends, override
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def work(self):
        print(f"{self.name} is working..")

        

class SoftwareEngineer(Employee):

    def __init__(self, name, age, salary, level):
        # call  the initializer 
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging..")

    def work(self):
        print(f"{self.name} is coding..")


class Designer(Employee):

    def draw(self):
        print(f"{self.name} is drawing..") 

    def work(self):
        print(f"{self.name} is designing..")


# create an instance of se
se = SoftwareEngineer("Marya",22,7000,"Senior")
print(se.name)
ds = Designer("Ali",22,4000)
ds.work()
se.work()
ds.draw()