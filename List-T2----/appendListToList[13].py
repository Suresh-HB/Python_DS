'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to append a list to the second list.
'''



def append_lists(list1, list2):   
    """
    Description: Function taking the Two input lists and adding list2 in to list1
    Parameter:
       list1, list2 : Function to taking as a parameter 
    Return: 
        list1 : returns after append list2 with list1
    """


    list1.extend(list2)
    return list1


def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    appended_list = append_lists(list1, list2)
    print("Appended List:", appended_list)


if __name__ == '__main__':
     main()

