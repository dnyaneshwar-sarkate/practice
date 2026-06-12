## Python programme to find teh longest word in the sentence

# text = ' Hello from Python!! Python is quite necessary these days in AI era'

# words = text.split(' ')

# longest = ''

# for i in words:
#     if len(i) > len(longest):
#         longest = i 

# print(longest)

##############################################################################################################################################################
text = ' Hello from Python!! Python is quite necessary these days in AI era'

longest = max(text.split(' '), key=len)
print(longest)