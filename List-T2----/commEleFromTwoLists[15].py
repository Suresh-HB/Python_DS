'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to find common items from two lists.
'''

def find_common_items(list1, list2):
    """
    Description: Function to find common items from two lists.
    Parameter:
       list1, list2 : Function taking (list1, list2) as a parameter in to the function.
    Return: 
        common_list :  returning the common elements from both as a list.
    """


    set1 = set(list1)
    set2 = set(list2)

    common_items = set1.intersection(set2)
    common_list = list(common_items)
    return common_list

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    common_items = find_common_items(list1, list2)
    print("Common items:", common_items)

if __name__ == '__main__':
    main()