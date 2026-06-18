## Python programme to reverse the number using floor division and modulo operator

number = 75642 

reversed_number = 0

while number > 0:

    #Get the last digit 
    digit = number % 10 

    #Add it to the revrse(shifting existing digits left) 
    reversed_number = (reversed_number * 10) + digit

    #Remove the last digit from the original number 
    number = number // 10 

print(reversed_number)