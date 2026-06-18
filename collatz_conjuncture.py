'''
Practice Problem: The Collatz conjecture states that if you start with any positive integer n, and if n is even, divide it by 2; if n is odd, multiply it by 3 and add 1. 
Repeat the process. The sequence will always eventually reach 1. Write a program to print this sequence for a given number.
'''

number = int(input('Enter a positive number: '))

while number != 1:
    
    if number % 2 == 0:
        number = int(number / 2)

    else:
        number = number * 3 + 1 
        
    print(number)