## Python programme to find the duplicates in the list 

lst = [1, 2, 3, 2, 5, 6, 3]

lst1 = [i for i in lst if lst.count(i) > 1]

res = sorted(set(lst1))
print(res)
