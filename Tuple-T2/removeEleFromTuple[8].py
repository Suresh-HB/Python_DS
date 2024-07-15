'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to convert list to tuple.
'''


def remove_item(t, item):
    """
    Description: Function to convert the given  list in to tuple
    Parameter: 
        t, item : function taking parameters for converting list form to tule form.
    Return:
       new_tuple: returning tuple form data 
    """

    new_tuple = tuple([x for x in t if x != item])
    return new_tuple


def main():
    my_tuple = (1, 2, 3, 4, 5)
    item_to_remove = 3
    new_tuple = remove_item(my_tuple, item_to_remove)
    print("Original Tuple:", my_tuple)
    print(f"Tuple after removing {item_to_remove}:", new_tuple)


if __name__ == '__main__':
    main()