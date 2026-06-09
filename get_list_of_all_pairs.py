##Python programme to get the list of all pairs from the given list elements 

# nums = [1, 2, 3]

# pairs = [(nums[i], nums[j]) 
#           for i in range(len(nums)) 
#           for j in range(i+1, len(nums))]

# print(pairs)

###################################################################################################################################
# from itertools import combinations

# nums = [1, 2, 3]

# pairs = list(combinations(nums, 2))
# print(pairs)

###################################################################################################################################

## Get all the ordered pairs including reverse

# nums = [1, 2, 3]

# pairs = [(i, j) for i in nums for j in nums if i != j]
# print(pairs)

##################################################################################################################################
## Pairs with condition(sum > 3)

# nums = [1, 2, 3]

# pairs = [(i, j) for i in nums for j in nums if i + j > 3]
# print(pairs)

####################################################################################################################################
## Unique pairs from duplicate list

from itertools import combinations
nums = [1, 2, 2, 3]

pairs = list(combinations(set(nums), 2))
print(pairs)