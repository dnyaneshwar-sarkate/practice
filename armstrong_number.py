## Python programme to find whether a number is armstrong no or not

'''
Armstrong Number :- An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits.
'''

# num = int(input('Enter a whole number: '))

# digits = str(num)
# power = len(digits)

# total = 0 

# for i in digits:
#     total = total + (int(i) ** power)

# if total == num:
#     print('Armstrong Number')
# else:
#     print('Not an Armstrong Number')

##################################################################################################################################################

num = int(input('Enter a whole number: '))

digits = str(num)
power = len(digits)

total = sum(int(i) ** power for i in digits)

if total == num:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')    