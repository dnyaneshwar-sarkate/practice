## Python programme to rotate a list by 'k' positions

def rotate_list(lst, k):
    if not lst:
        return lst # Handles empty List
    
    k = k % len(lst)

    if k == 0:
        return lst 
    
    return lst[-k:] + lst[:-k]


if __name__ == '__main__':

    lst = [int(i) for i in input('Enter comma seperated list of numbers: ').split(',')]
    k = int(input('Want to rorate list by how many positions? '))

    res = rotate_list(lst, k)
    print(res)