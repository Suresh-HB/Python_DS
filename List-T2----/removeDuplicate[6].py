'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Program to remove the duplicates from the given list.
'''

def remove_duplicates(input_list):
    """
    Description: Function to remove the duplicates form the given list
    Parameter:
       input_list: Function taking (input_list) as a parameter in to the function
    Return: 
        result: returning the distinct list 
    """
    unique_elements = set()
    result = []
    

    for item in input_list:
        if item not in unique_elements:
            unique_elements.add(item)
            result.append(item)
    return result

def main():
    sample_list = [6,2,1, 2, 3, 1, 2, 5, 6, 7, 8, 1,5]
    print("Original List:", sample_list)
    unique_list = remove_duplicates(sample_list)
    print("List with Duplicates Removed:", unique_list)

if __name__ == '__main__':
    main()
