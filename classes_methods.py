# Without OOP
print('without oop')
se = ["Software Engineer", "Max", 20, "Junior", 5000]
d1 = ["doctor", "Lisa", 25, "mid-level", 7000]

# define a global function
def code(se):
    print(f"{se[1]} is writing code ..")
# function call
code(se)
code(d1)
# the function are called to many objects,
#  but what if we want the function just to be called by software engineers?


# With OOP
print('with oop')
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

    # for every instance method we have to write self
    def code(self):
        print(f"{self.name} is writing code ..")

    # overloading
    def code_in(self, language):
        print(f"{self.name} is writing code in {language}")
        

# Third: create an instance of a class 
se = SoftwareEngineer("Max", 20, "Junior", 5000)
se.code()
se.code_in("python")


