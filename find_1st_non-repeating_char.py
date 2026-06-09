##Python programme to find first non-repeating character

'''
Ex. s = "aabbccde"
-> d
'''

text1 = 'aabbccde'

for i in text1:
    if text1.count(i) == 1:
        print(i)
        break