## Python programme to find the smallest and largest element in the list 

# Using Built-in Functions - min, max
# lst = [-20, 0, 10, -5, 6, 8.9, 16]

# smallest, largest = min(lst), max(lst)
# print(f"Smallest number: {smallest} \nLargest number: {largest}")

###########################################################################################################################################

# Using sorted()

# smallest = sorted(lst)[0]
# largest = sorted(lst, reverse = True)[0]

# print(f"Smallest number: {smallest} \nLargest number: {largest}")

#############################################################################################################################################

# Using for loop

lst = [-20, 0, 10, -5, 6, 8.9, 16]

smallest = lst[0]
largest = lst[0]

for i in lst:
    if i < smallest:
        smallest = i 
    
    if i > largest:
        largest = i 

print(f"Smallest number: {smallest} \nLargest number: {largest}")