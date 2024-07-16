'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to print a specified list after removing the 0th, 4th and
5th elements. 
'''



# Remove the 0th, 4th, and 5th elements
# Note that we should remove the elements in reverse order to avoid index shifting issues
def deletionElements(sample_list):
    """
    Description: Function taking the input list and removing the specified indexed elements 
                from the give list by using del key word 
    Parameter:
       sample_list : Function to taking as a parameter for remove the specified elements
    Return: 
    """
    
    
    del sample_list[5]
    del sample_list[4]
    del sample_list[0]


def main():
    sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    deletionElements(sample_list)
    print(sample_list)


if __name__ == '__main__':
    main()