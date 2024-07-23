'''

@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Counting the Occurrence of given element

'''

import loggingfile
import os


current_scriptname=os.path.basename(__file__)

logger=loggingfile.logg(current_scriptname)
              
def count_occurrences(arr, element):
    """
    Description: Function to count the Occurrence of the incoming element
    Parameter: 
        arr, element : function takes one array and one element
    Return:
       count: returning the count of specified element 
    """

    logger.info("inside count_occurrences method")

    count = 0
    for item in arr:
        if item == element:
            count += 1
    logger.debug(f"{count} times the given element present and this method returning count")
    return count


def main():

    logger.info("Inside main method")
    
    arr = [1, 2, 3, 4, 2, 2, 3, 1, 1]
    logger.debug(f"{arr} is the input")
    element = 2
    logger.debug("calling count_occurrences method")
    print(f"Number of occurrences of {element} in the array: {count_occurrences(arr, element)} times")


if __name__ == "__main__":
    main()