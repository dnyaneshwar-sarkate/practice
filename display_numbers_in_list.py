'''Practice Problem: Given a list of numbers, iterate through it and print numbers that satisfy these conditions:

Conditions:
The number must be divisible by five.
If the number is greater than 150, skip it and move to the next.
If the number is greater than 500, stop the loop entirely.
'''

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break 
    
    if i > 150:
        continue 

    if i % 5 ==0:
        print(i)