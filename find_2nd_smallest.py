##Python programme to find second smallest number

lst = [float(i) for i in input("Enter comma seperated list of numbers: ").split(',')]

def find_2nd_smallest_no(lst):
    smallest = second_smallest = float('inf')

    for i in lst:
        if i < smallest:
            second_smallest = smallest 
            smallest = i 
        elif i < second_smallest and i!= smallest:
            second_smallest = i
    return second_smallest

if __name__ == "__main__":
    result = find_2nd_smallest_no(lst)
    print(f"Second smallest number is: {result}")