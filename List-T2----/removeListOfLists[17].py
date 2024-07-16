'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to remove duplicates from a list of lists.
'''

def remove_duplicates_from_list_of_lists(list_of_lists):
    """
    Description: Function to remove the duplicates from the list of lists.
    Parameter:
       list_of_lists : Function to taking as a parameter 
    Return: 
        new_list_of_lists : returns the new list as unduplicated list
    """

    seen = set()
    new_list_of_lists = []
    
    for sublist in list_of_lists:
        tuple_sublist = tuple(sublist)
        if tuple_sublist not in seen:
            seen.add(tuple_sublist)
            new_list_of_lists.append(list(tuple_sublist))
    return new_list_of_lists

def main():

    sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    new_list = remove_duplicates_from_list_of_lists(sample_list)
    print("New List:", new_list)


if __name__ == '__main__':
    main()
