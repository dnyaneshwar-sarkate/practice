##Python programme to find top 3 frequent elements

def find_top3_freq_elem(lst):
    freq = {} #Initailised empty dictionary
    for i in lst:
        freq[i] = freq.get(i, 0) + 1

    #Sort the dictionary KEYS based on theier values
    sorted_lst = sorted(freq, key=freq.get, reverse = True) 

    #Extract the first 3 elements
    res_lst = sorted_lst = sorted_lst[0:3]

    return res_lst

if __name__ == "__main__":
    lst = [int(i.strip()) for i in input('Enter a comma seperated list of elements:').split(',')]

    result = find_top3_freq_elem(lst)
    print(f"sorted list: {result}")