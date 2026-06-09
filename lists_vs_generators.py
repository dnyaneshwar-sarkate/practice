## Python programme to differentiate between list and geneartors

#List 
lst = [i*i for i in range(1, 11)]

print(type(lst))
print(lst)

# Generators
gen = (i*i for i in range(1, 11))
print(type(gen))

for i in gen:
    print(i, end =' ')