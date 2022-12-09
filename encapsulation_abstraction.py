# encapsulation 
# is the mechanism of hiding the data implementation 
# in which instance variables are kept private and there is one way to reach
# using public methods setters and getters
# private methods can only be used inside the class


class SoftwareEngineer():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # private attribute
        # one _ not completely private
        # two __ are completely private
        self._salary = None
        self._num_bugs_solved = 0
    
    def work(self):
        print(f"{self.name} is working..")

    def get_salary(self):
        return self._salary
    
    def set_salary(self, base_sal):
        self._salary = base_sal

    # private method
    def _calculate_salary(self, base_sal):
        if self._num_bugs_solved<10:
            return base_sal
        if self._num_bugs_solved<100:
            return base_sal*2

        return base_sal

se = SoftwareEngineer("Marya",22)
se.set_salary(6000)
print(se.get_salary())
        
# why is that useful?
# we can check the value, or add constrains
# add password

# ----------------------
# abstraction
# hiding the implementation of the class 
#  