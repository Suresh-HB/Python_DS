'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Removing items from set
'''


def removeItems(set1):
    """
    Description: Function to remove the elements present in the set
    Parameter: Function takes the set1 as a parameter 
    Return: 
    """


    print(set1," Before remove")

    while set1:
        # print(max(set1), 'removed')
        # set1.discard(max(set1)) 
        removed_ele = set1.pop()
        print(removed_ele, 'removed')
    print(set1," After removed")


def main():
    set1={10,20,60,40,8,296,56,45}
    removeItems(set1)


if __name__ == '__main__':
    main()