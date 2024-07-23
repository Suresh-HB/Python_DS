'''

@Author: Suresh
@Date: 2024-07-11 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Reverse the order of items in the Array.

'''

import loggingfile
import os
import array

current_scriptname=os.path.basename(__file__)

logger=loggingfile.logg(current_scriptname)




def reverse():
    """
    Description: Function  to iterate array elements in backward direction from last index position to frist and prints that array
    Parameter: 
    Return:
    """   

    logger.info("Inside reverse method")

    array_of_integers = array.array('i',[10, 20, 30, 40, 50])
    logger.debug(f"this is the actual array{array_of_integers}")

    print("Original array:--->", array_of_integers)
    
    reversed_array = array_of_integers[::-1]
    logger.info("reversing the array elements")

    array2_integers =reversed_array

    print("Reversed array:--->", array2_integers )
    logger.debug(f"Array elements are reversed{array2_integers}")


def main():
    logger.info("Inside main method")
    reverse()

if __name__ =='__main__':
    reverse()