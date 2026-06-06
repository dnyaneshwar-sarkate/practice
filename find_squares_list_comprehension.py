##Python programme to find the squares of numbers inside the list 

lst = [float(i) for i in input('Enter comma seperated list of numbers: ').split(',')]

def find_squares(lst):
    squares_of_negative_nos = [round(i*i, 2) for i in lst if i < 0]
    squares_of_positive_nos = [round(i*i, 2) for i in lst if i > 0]

    return squares_of_positive_nos, squares_of_negative_nos

if __name__ == '__main__':
    pos_squares, neg_squares = find_squares(lst)
    print(f"Squares of positive numbers entered: {pos_squares}", end = '\n'
          f"Squares of negative numbers entered: {neg_squares}")