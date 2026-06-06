# ##Python programme to merge dictionaries

dict1 = {'a':10, 'b':15, 'c':20}
dict2 = {'b':60, 'c':10, 'd':100}

def merge_dic(dict1, dict2):
    result = dict1.copy()

    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result 

if __name__ == '__main__':
    res_dict = merge_dic(dict1, dict2)
    print(f"Merged dictionary: {res_dict}")