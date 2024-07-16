'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Program to clone the list and return that list. 
'''


def Cloning(li1):
    """
    Description: Function to takes the coling list and returns that list  
    Parameter: Function to taking the list (li1) as a parameter
    Return: 
    """


    li_copy = li1[:]
    print("After Cloning:", li_copy)
 
def main():
    li1 = [4, 8, 2, 10, 15, 18]
    Cloning(li1)
    print("Original List:", li1)


if __name__ == '__main__':
    main()
