'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Program to create an intersection of sets
'''


def createIntersectSet():
    """
    Description: Function finds a set that contains the similarity between two or more sets. 
    Parameter: 
    Return: 
    """

    
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    z = x.intersection(y)
    print(z)


def main():
    createIntersectSet()


if __name__ == '__main__':
    main()