## Python Programme to find teh GCD of two numbers 

'''
GCD (Greatest Common Divisor) is the largest number that divides both numbers without leaving a remainder.
Ex. GCD(12, 18) :- 6
'''

# def gcd(num1, num2):

#     lst1 = []

#     for i in range(2, int(num1 / 2) + 1):
#         if num1 % i == 0:
#             lst1.append(i)
    
#     lst2 = []

#     for j in range(2, int(num2 / 2) + 1):
#         if num2 % j == 0:
#             lst2.append(j)

#     result = []
#     for i in lst1:
#         if i in lst2:
#             result.append(i)

#     return max(result)

# if __name__ == '__main__':

        
#     num1 = int(input('Enter 1st number - Positive Integer: '))
#     num2 = int(input('Enter 2nd number - Postive Integer: '))

#     result = gcd(num1, num2)

#     print(f'GCD: {result}')

########################################################################################################################################################

def gcd(num1, num2):

    gcd = 1

    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i 
    
    return gcd

print(gcd(12, 18))