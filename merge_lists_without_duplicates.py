## Python programme to merge two lists without duplicates 

# Using extend method
# lst1 = [1, 2, 3, -9, 5, 8]
# lst2 = [1, 2, -9, 11, 12]

# lst1.extend(lst2)
# print(list(set(lst1)))

################################################################################################################################################################

# Using set()

# result = list(set(lst1 + lst2))
# print(result)

################################################################################################################################################################

# Preserve Order

# lst1 = [1, 2, 3, -9, 5, 8]
# lst2 = [1, 2, -9, 11, 12]

# joined_lst = lst1 + lst2 

# result = []

# for i in joined_lst:
#     if i not in result:
#         result.append(i)

# print(result)

################################################################################################################################################################

# Using dict.fromkeys() --> this creates a dictionary with list values as keys and None value as dictionary values 

lst1 = [1, 2, 3, -9, 5, 8]
lst2 = [1, 2, -9, 11, 12]

result = list(dict.fromkeys(lst1 + lst2))
print(result)