## Python programme to check whether thw two strings are anagram or not

# def check_anagram(str1, str2):

#     str1 = str1.replace(' ', '').lower()
#     str2 = str2.replace(' ', '').lower()

#     if sorted(str1) == sorted(str2):
#         return 'Anagrams!'
#     else:
#         return 'Not Anagrams!'
    
# if __name__ == '__main__':

#     str1 = input('Enter first string: ')
#     str2 = input('Enter second string: ')

#     result = check_anagram(str1, str2)
#     print(result)

##########################################################################################################################################################

from collections import Counter

str1 = input('Enter first string: ')
str2 = input('Enter second string: ')

if Counter(str1.replace(' ', '').lower()) == Counter(str2.replace(' ', '').lower()):
    print('Anagram!')
else:
    print('Not Anagram!')