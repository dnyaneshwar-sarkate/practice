##Python programme to check if the list is sorted or not

lst = [1 ,2, 3, 4, 5, 6, 4]


# is_sorted = False

# if lst == sorted(lst):
#     is_sorted = True
#     print(is_sorted)
# else:
#     print(is_sorted)


####################################################################################################################################################
## Using list comprehension

lst = [1, 2, 3, 4, 5]

is_sorted = all (lst[i] <= lst[i+1] for i in range(len(lst) - 1))
print(is_sorted)