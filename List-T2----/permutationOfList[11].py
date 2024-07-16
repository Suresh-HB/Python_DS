'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to generate all permutations of a list in Python.
'''


import itertools


def permutation(sample_list):
    """
    Description: Function taking the input given list and prforming the permutation operation
    Parameter:
       sample_list : Function to taking as a parameter 
    Return: 
    """
        

    permutations = list(itertools.permutations(sample_list))
    for perm in permutations:
        print(perm)


def main():
    sample_list = ['Red', 'Green', 'Blue']
    permutation(sample_list)


if __name__ == '__main__':
    main()
 

