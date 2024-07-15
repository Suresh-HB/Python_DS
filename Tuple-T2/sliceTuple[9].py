'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to iterate the tuple using slicing.
'''


def slice_tuple(t, start, stop, step):
    sliced_tuple = t[start:stop:step]
    return sliced_tuple


def main():
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    start_index = 2
    stop_index = 7
    step_size = 2
    sliced_result = slice_tuple(my_tuple, start_index, stop_index, step_size)
    print("Original Tuple:", my_tuple)
    print("Sliced Tuple:", sliced_result)


if __name__ == '__main__':
    main()
