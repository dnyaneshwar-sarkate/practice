## Python programme to demonstrate the working of global variable 

global_variable = 10 

def modify_variable():

    global global_variable # Access global variable inside the function

    global_variable = 20 

print("Initial: ", global_variable)
modify_variable()
print("After: ", global_variable)