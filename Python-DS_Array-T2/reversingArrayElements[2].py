'''

@Author: Suresh
@Date: 2024-07-11 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Reverse the order of items in the Array.

'''


import array

def reverse():
    """
    Description: Function  to iterate array elements in backward direction from last index position to frist and prints that array
    Parameter: 
    Return:
    """   


    array_of_integers = array.array('i',[10, 20, 30, 40, 50])

    print("Original array:--->", array_of_integers)
    
    reversed_array = array_of_integers[::-1]
    array2_integers =reversed_array

    print("Reversed array:--->", array2_integers )


def main():
    reverse()

if __name__ =='__main__':
    reverse()