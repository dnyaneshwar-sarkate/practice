##Python programme to demonstrate working of break statement inside the loop --> Programme to find a number in the list

def find_no(lst):
    for i in lst:
        if i == num:
            print("Found!!")
            break 
        print(i)

if __name__ == "__main__":
    lst = [float(i.strip()) for i in input("Enter a list of comma seperated numbers: ").split(',')]
    num = float(input('Enter the number to find out: '))
    find_no(lst)