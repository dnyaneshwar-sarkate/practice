##Python programme to remove the duplicates

nums = [float(i) for i in input("Enter comma seperated numbers: ").split(',')]

def remove_duplicates(nums):
    unique_values = []
    for i in nums:
        if i not in unique_values:
            unique_values.append(i)
    return unique_values

if __name__ == '__main__':
    result = remove_duplicates(nums)
    print(result)


## Alternate approach
# nums = [float(i) for i in input("Enter comma seperated numbers: ").split(',')]

# unique_list = list(set(nums))
# print(unique_list)