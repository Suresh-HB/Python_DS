'''
@Author: Suresh
@Date: 2024-07-11 
@Last Modified by: Suresh
@Last Modified: 2024-07-11
@Title : Removing the frist Occurrence of the element
'''

import os
import loggingfile

current_scriptName=os.path.basename(__file__)
logger=loggingfile.logg(current_scriptName)

def remove_first_occurrence(arr, element):
    """
    Description: Function to remove the element found at frist occurrence
    Parameter: 
        arr, element : function takes one array and one element
    Return:
    """
    logger.info("Inside remove_first_occurrence method")

    if element in arr:
        arr.remove(element)
        logger.debug(f"{element} is removed")



def main():

    logger.info("Inside main method")
    arr = [1, 2, 3, 4, 2, 2, 3, 1, 1]
    logger.debug(f"{arr} given array")
    element = 2
    logger.debug(f"given element for remve occurrences {element} ")

    print("**Original array** :----> ", arr)

    logger.info("Calling remove_first_occurrence method")
    remove_first_occurrence(arr, element)
    print("**Array after removed** :--->", element, ":", arr)

if __name__ == '__main__':
    main()