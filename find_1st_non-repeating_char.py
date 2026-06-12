##Python programme to find first non-repeating character

'''
Ex. s = "aabbccde"
-> d
'''

# text1 = 'aabbccde'

# def find_1st_non_repeating_char(text1):
#     for i in text1:
#         if text1.count(i) == 1:
#             return i
#             break
#     else:
#         return 'Not Found!'
    
# print(find_1st_non_repeating_char(text1))


##########################################################################################################################################################
# Using List Comprehension 

# res = [i for i in text1 if text1.count(i) == 1]
# print(res[0])