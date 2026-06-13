## Python programme to find the prime numbers in a given range of number

num1 = int(input('From Number: '))
num2 = int(input('To Number: '))

primes = []

for i in range(num1, num2 + 1):

    if i < 2:
        continue

    is_prime = True  # Initailly assume number is Prime 

    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False 
            break
    
    if is_prime:
        primes.append(i)

print(primes)