## Python prgramme to find the smallest and largest number 

num = int(input('Enter a positive number: '))

# Initialize with opposite extremes
largest = float('-inf')
smallest = float('inf')

while num > 0:
    digit = num % 10
    
    # Check for new largest
    if digit > largest:
        largest = digit
    # Check for new smallest
    if digit < smallest:
        smallest = digit
        
    num = num // 10

print("Largest digit:", largest)
print("Smallest digit:", smallest)