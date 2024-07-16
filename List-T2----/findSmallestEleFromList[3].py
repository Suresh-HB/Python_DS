'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Program to find the smallest element from the given list.
'''


def sumListElements(list1): 
    """
    Description: Function to finds the smallest element present in the given list and prints that element
    Parameter: Function to taking the list (list1) as a parameter
    Return: 
    """


    small=list1[0]
    for ele in list1:
        if small>ele:
            small=ele
    print(small," ---> is the smallest element present in the  given list")


def main():
    list1=[10,8,20,30,40,50,60,70,80,7]
    sumListElements(list1) 


if __name__ == '__main__':
    main()