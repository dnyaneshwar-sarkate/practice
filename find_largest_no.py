##Python programme to find the largest number

nums = [float(i) for i in input("Enter a comma seperated list of numbers: ").split(',')]

def largest_no(nums):
    largest_no = 0
    for i in nums:
        if i > largest_no:
            largest_no = i
    return largest_no

if __name__ == '__main__':
    print("Largest no is", largest_no(nums))