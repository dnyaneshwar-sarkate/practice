## Python programme to generate the Fibonacci series

# Using Generators
# def fibonacci(num):
#     a, b = 0, 1

#     for _ in range(num):
#         yield a
#         a, b = b, a+b 

# for i in fibonacci(8):
#     print(i, end = ' ')

##########################################################################################################################################################

num = int(input('Enter a number: '))
a, b = 0, 1
for _ in range(num):

    print(a)
    a, b = b, a+b