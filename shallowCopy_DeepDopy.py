##Python programme to distingusih between shallow copy and deep copy

import copy

# Shallow Copy --> creates new ouetr objects but the nested objects inside are still shared

# original = [[1, 2], [3, 4]]

# shallow = copy.copy(original)

# shallow[0].append(99)

# print("Original: ", original)
# print("Shallow: ", shallow) #Cause it points to the same inner list


## Deep Copy --> Creates a completely independent copy, including all the nested objects 
original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)

deep[0].append(99)

print("Original: ", original)
print("Deep: ", deep)