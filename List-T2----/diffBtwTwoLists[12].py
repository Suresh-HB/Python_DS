'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to get the difference between the two lists.
'''


def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    difference = list(set(list1) - set(list2))
    print("Difference:", difference)


if __name__ == '__main__':
    main()