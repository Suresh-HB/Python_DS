'''

@Author: Suresh
@Date: 2024-07-11
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Creating and iterating array elements

'''

import array
import loggingfile
import os

current_scriptname=os.path.basename(__file__)
logger=loggingfile.logg(current_scriptname)


def arrayCreating():
    """
    Description: Function to iterates the elements present in the Array and prints based on indexs
    Parameter: 
    Return:
    """

    logger.info("Inside arrayCreation method")
    arr=array.array('i',[10, 20, 30, 40, 50])
    logger.debug(f"Array get created arr = {arr}")
    
    print("Array elements based on index:")
    for i in range(len(arr)):
        print(f"Element at index {i} = {arr[i]}")

    logger.info(f"Array is created and printed{arr}")
    


def main():
    
    logger.info("Inside main method")
    logger.info("calling arrayCreation method")

    arrayCreating()
   

if __name__ == '__main__':
    main()
