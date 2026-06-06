# ##Python programme to check if the string is palindorm or not

# text = input("Enter a string:")

# def palindorme_check(text):
#     reversed_str = text[::-1]

#     if text == reversed_str:
#         print("Palindrome!!")
#     else:
#         print("Not a palindorme")

# if __name__ == "__main__":
#     palindorme_check(text)


##########################################################################
txt = input("Enter a string:")

def palindrome_check(txt):
    reversed_str = ''
    for i in reversed(txt):
        reversed_str = reversed_str+i
    if txt == reversed_str:
        print("palindrome!!")
    else:
        print("Not a palindoeme")

palindrome_check(txt)