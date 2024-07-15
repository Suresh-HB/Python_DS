'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : To find minimum and maximum element from the set
'''


def findMinMax():
    """
    Description: Function to find the maximum and value from the given set 
                 and prints that values
    Parameter: 
    Return: 
    """


    sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55])
    print(max(sets))
    print(min(sets))


def main():
    findMinMax()


if __name__ == '__main__':
    main()