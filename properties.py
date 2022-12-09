# properties 
# giving setters and getters the same name as the o[private attribute
# but without the underscore, and adding @ decorator

class SoftwareEngineer():
    def __init__(self):

        self._salary = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, base_sal):
        self._salary = base_sal

    @salary.deleter
    def salary(self):
        del self._salary



se = SoftwareEngineer("Marya",22)
se.salary = 6000
print(se.get_salary())
        
