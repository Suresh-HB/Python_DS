'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to reverse the given tuple.
'''


def reverse_tuple(t):
    reversed_tuple = tuple(reversed(t))
    return reversed_tuple


def main():
    my_tuple = (1, 2, 3, 4, 5)
    reversed_result = reverse_tuple(my_tuple)
    print("Original Tuple:", my_tuple)
    print("Reversed Tuple:", reversed_result)


if __name__ == '__main__':
    main()