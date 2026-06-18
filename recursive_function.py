## Python programme to calculate sum of number sfrom 1 to 10 using recursion

def addition(num):
    
    #Recursive case: Add current num to the result fo the addition(num - 1)
    if num:
        return num + addition(num - 1)
    
    else:
        return 0
    
result = addition(10)

print(result)
