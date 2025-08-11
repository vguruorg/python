import sys

myboard_len = 9
#myboard = [ [i+1 for x in range(myboard_len)] for i in range(myboard_len)]
'''
myboard = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9] 
]
'''
myboard = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [7, 7, 7, 7, 7, 7, 7, 7, 7],
    [8, 8, 8, 8, 8, 8, 8, 8, 8],
    [9, 9, 9, 9, 9, 9, 9, 9, 9] 
]
 
def build_row_list(myboard, myboard_len):
    row_list = myboard.copy()
    return row_list

def build_col_list(myboard, myboard_len):
    col_list = [ [0 for x in range(myboard_len)] for i in range(myboard_len)]

    for col_index in range(myboard_len):
        for row_index in range(myboard_len):
            col_list[col_index][row_index] = myboard[row_index][col_index]

    return col_list

def build_box_list(myboard, myboard_len):
    box_list = [ [0 for x in range(myboard_len)] for i in range(myboard_len)]
    row_index = 0
    while (row_index < myboard_len):
        col_index = 0
        while(col_index < myboard_len):
            box_no = (int(row_index / 3) * 3) + int(col_index / 3)
            seq_no = (int(row_index % 3) * 3) + int(col_index % 3)
            #print(f"({row_index}, {col_index})= Box[{box_no}][{seq_no}] ")
            box_list[box_no][seq_no] = myboard[row_index][col_index]
            #myboard[row_index][col_index] = box_no
            col_index +=1
        row_index +=1
    return box_list

def is_list_valid(suduko_list):
    global myboard_len

    if(len(suduko_list)  != myboard_len):
        return False

    temp_list = [False for x in range(myboard_len)]
    for elem in suduko_list:
        if (elem < 1 or elem > 9):
            return False
        else:
            if(temp_list[elem-1] == True):
                return False
            else:
                temp_list[elem-1] = True
    
    all_true = True
    for value in temp_list:
        if(value == False):
            all_true = False
            break
    return all_true


def is_board_valid(myboard, myboard_len):
    is_valid = True

    print("Validating - Started ...")
    print("Validating - Rows ...")
    row_list = build_row_list(myboard, myboard_len)
    for single_list in row_list:
        #print(single_list)
        #print(is_list_valid(single_list))
        is_valid = is_list_valid(single_list)
        print(single_list, end = " ")
        print(is_valid)
        if(is_valid == False):
            return False

    print("Validating - Cols ...")
    col_list = build_col_list(myboard, myboard_len)
    for single_list in col_list:
        #print(is_list_valid(single_list))
        is_valid = is_list_valid(single_list)
        print(single_list, end = " ")
        print(is_valid)
        if(is_valid == False):
            return False

    print("Validating - Boxes ...")
    box_list = build_box_list(myboard, myboard_len)
    for single_list in box_list:
        #print(single_list)
        #print(is_list_valid(single_list))
        is_valid = is_list_valid(single_list)
        print(single_list, end = " ")
        print(is_valid)
        if(is_valid == False):
            return False

    print("Validating - Completed.")
    return is_valid



for row in myboard:
    print(row)
    pass

print(is_board_valid(myboard, myboard_len))