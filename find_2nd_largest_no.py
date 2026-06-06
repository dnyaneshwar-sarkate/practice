##Python programme to find 2nd largest number

lst = [float(i) for i in input("Enter a comma seperated list of numbers: ").split(',')]

def find_2nd_largest_num(lst):
    largest_num = second_largest_num = float("-inf")

    for i in lst:
        if i > largest_num:
            second_largest_num = largest_num
            largest_num = i
        elif (i > second_largest_num) and (i != largest_num):
            second_largest_num = i
    return second_largest_num 

if __name__ == "__main__":
    result = find_2nd_largest_num(lst)
    print(f"Second largest number is: {result}")