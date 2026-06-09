##Python programme to find missing nos from 1 to 100

lst1 = list(range(1,101))
lst2 = list(range(1, 91))


# lst = []
# for i in lst1:
#     if i not in lst2:
#         lst.append(i)

# print(lst)

##########################################################################################################################################
## Using list comprehension

lst1 = list(range(1,101))
lst2 = list(range(1, 91))

res = [i for i in lst1 if i not in lst2]
print(res)