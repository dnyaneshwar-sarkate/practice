'''Python programme to check whether the given number is perfect or not

A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself). For example, 6 is perfect because 1 + 2 + 3 = 6.
'''

num = int(input('Enter a number: '))

# A diviosr cannot be greater than the half of the number
def find_perfect_no(num):
    divisor_sum = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            divisor_sum = divisor_sum + i 
    
    if num == divisor_sum:
        return 'Perfect Number!'
    else:
        return 'Number is not perfect'
    
print(find_perfect_no(num))