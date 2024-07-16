'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to check whether two lists are circularly identical.
'''


def are_lists_circularly_identical(list1, list2): 
    """
    Description: Function to check whether two lists are circularly identical.
    Parameter:
       list1, list2 : Function taking (list1, list2) as a parameter in to the function
    Return: 
        rst2 :  returning the identical list result
    """


    if len(list1) != len(list2):
        return False
    
    str1 = ''.join(map(str, list1))
    str2 = ''.join(map(str, list2))
    return str2 in str1 + str1


def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 1, 2]
    result = are_lists_circularly_identical(list1, list2)
    if result:
        print("Lists are circularly identical.")
    else:
        print("Lists are not circularly identical.")


if __name__ == '__main__':
    main()
