'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to check given element exists within a tuple.
'''


def element_exists(t, element):  
    """
    Description: Function to identify the element which is present in the tuple returns.
    Parameter: 
        t : Function taking the parameter as a tuple.
    Return: 
        repeated_items : Function returning the repeated values as a list
    """

    return element in t


my_tuple = (1, 2, 3, 4, 5)
element_to_find = 3
exists = element_exists(my_tuple, element_to_find)


if exists:
    print(f"{element_to_find} exists in the tuple.")
else:
    print(f"{element_to_find} does not exist in the tuple.")
