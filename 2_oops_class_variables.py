## Python programme to demonstarte the working of class variables and how they differ from instance variables

class Employee:

    # Class Variable
    raise_amount = 1.04
    no_of_emps = 0 # Number of employees are gonna remain the same for all the instances of the class, isn't it?

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Each time an instance is created, increment class variable by 1 
        Employee.no_of_emps = Employee.no_of_emps + 1 # See we accessed class variable with the class name here


    def fullname(self):
        return f'{self.first} + ' ' + {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Linus', 'Torvalds', 80000)
emp_2 = Employee('Test', 'User', 60000)

# To get the namespace of an instance of the class 
# print(emp_1.__dict__)

# To print the namespace of a class
# print(Employee.__dict__)


''' Note --> When we create an instance of a partiulat class, it will first check whether the given class contain that attribute, 
        if yes then it will considered.
            If the instance doesn't contain that attribute, then it will check into the class

            In short - Priority will be given to instance variable over the class variables
'''


# change the class variable - set other value
# Employee.raise_amount = 1.05
# print(Employee.raise_amount)

## Change the class variable from an instance of the class
# emp_1.raise_amount = 1.06

# print(Employee.raise_amount)
# print(emp_1.raise_amount) # Here it uses, emp_1's raise_amount instaed of class's raise_amount, cause we changed it manually in previous line of code
# print(emp_2.raise_amount)

# print(emp_1.raise_amount)
# emp_1.apply_raise()
# print(emp_1.pay)

print(Employee.no_of_emps)

# Create another instance to test 
emp_3 = Employee('John', 'Hamm', 150000)

print(Employee.no_of_emps)