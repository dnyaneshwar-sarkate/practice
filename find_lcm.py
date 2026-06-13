## Python programme to find the LCM of two numbers 

'''
LCM (Least Common Multiple) is the smallest positive number that is divisible by both numbers.
Ex. LCM(12, 18) :- 36
'''

def lcm(num1, num2):

    greater = max(num1, num2)

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            return greater 
        
        greater = greater + 1

print(lcm(12, 18))