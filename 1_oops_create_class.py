## Python programme to generate employee class

class Employee:

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last 
    
# Calling the method using Instance of the class

emp1 = Employee('Linus', 'Torvalds', 70000)
emp2 = Employee('Test', 'User', 60000)

# print(emp1.fullname())
# print(emp2.fullname())


# Calling the method using the class itself

print(Employee.fullname(emp1))