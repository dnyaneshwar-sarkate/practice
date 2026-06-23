## Programme to create a function print_info(**kwargs) that accepts an arbitrary number of keyword arguments and prints the key-value pairs.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'key:{key} value:{value}')

print_info(name="Alice", age=30, city="New York")