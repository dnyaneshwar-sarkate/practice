'''Python programme to calculate the function with different name

Functions --> 1st class objects -> can be passed as arguments, returned from another function or renamed
'''

def display_students(name, age):
    return name, age

display = display_students

print(display('John', 13))
