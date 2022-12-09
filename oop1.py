# First: why we need OOP?
# to represent a software engineer we can use a list

# position, name, age, name, level, salary
se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 25, "Senior", 7000]
# when we have multiple objects with the same parameters, it's easy to make mistakes and repetition 
# classes are used to represent objects and there behaviors using attributes and methods
# a class is a blueprint of a data structure 

# Second: How to Create a Class?
class SoftwareEngineer:
    
    # class attribute: shared (belong to the class)
    alias = "Keyboard Magician"

    # constructors
    def __init__(self, name, age, level, salary):
        # instance attribute, not shared ( only belongs to one object)
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        

# Third: create an instance of a class 
se3 = SoftwareEngineer("Max", 20, "Junior", 5000)
print(se3.name, se3.age)
se4 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
print(se4.alias)