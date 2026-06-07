##Python programme to demonstrate the working of continue statement in the conditional loop

lst = [int(i.strip()) for i in input('Enter comma seperated list of numbers: ').split(',')]
num = int(input('Enter the number whcih you want to find out: ').strip())

def find_no(lst):
    for i in lst:
        if i == num:
            print("Found!")
            continue
        print(i)

find_no(lst)