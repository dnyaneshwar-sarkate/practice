## Python programme to find dictionary key with the maximum value

i_dict = {
    'Alice': 25,
    'Bob': 30, 
    'John': 60,
    'Maria': 22
}

############################################################################################################################################################

# result = list(sorted(i_dict, key=i_dict.get, reverse = True))
# print(result[0])

############################################################################################################################################################

key = max(i_dict, key=i_dict.get)

print(key, i_dict[key], sep = ', ')