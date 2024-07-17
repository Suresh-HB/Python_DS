'''
@Author: Suresh
@Date: 2024-07-11 
@Last Modified by: Suresh
@Last Modified: 2024-07-11
@Title : Removing the frist Occurrence of the element
'''


def remove_first_occurrence(arr, element):
    """
    Description: Function to remove the element found at frist occurrence
    Parameter: 
        arr, element : function takes one array and one element
    Return:
    """


    if element in arr:
        arr.remove(element)


def main():
    arr = [1, 2, 3, 4, 2, 2, 3, 1, 1]
    element = 2

    print("**Original array** :----> ", arr)
    remove_first_occurrence(arr, element)
    print("**Array after removed** :--->", element, ":", arr)

if __name__ == '__main__':
    main()