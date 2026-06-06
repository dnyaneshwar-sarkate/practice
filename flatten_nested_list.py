##Python programme to flatten the nested list 

nested_lst = [[1,2],[3,4],[5,6], 100,[1,2,8,9,15]]

def flatten_nested_lst(lst):
    res_lst = []
    for i in nested_lst:
        if isinstance(i, list):
            for j in range(len(i)):
                res_lst.append(i[j])
        else:
            res_lst.append(i)
    return res_lst 

if __name__ == '__main__':
    print(flatten_nested_lst(nested_lst))