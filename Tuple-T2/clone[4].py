'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to clone the tuple.
'''

def create_colon(t):
    colon_tuple = tuple(reversed(t))
    return colon_tuple


def main():
    original_tuple = (1, 2, 3, 4, 5)
    colon_tuple = create_colon(original_tuple)
    print("Original Tuple:", original_tuple)
    print("Colon Tuple:", colon_tuple)


if __name__ == '__main__':
    main()
