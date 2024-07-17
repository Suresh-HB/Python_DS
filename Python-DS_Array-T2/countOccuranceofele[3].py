'''

@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Counting the Occurrence of given element

'''


def count_occurrences(arr, element):
    """
    Description: Function to count the Occurrence of the incoming element
    Parameter: 
        arr, element : function takes one array and one element
    Return:
       count: returning the count of specified element 
    """


    count = 0
    for item in arr:
        if item == element:
            count += 1
    return count


def main():
    
    arr = [1, 2, 3, 4, 2, 2, 3, 1, 1]
    element = 2
    print(f"Number of occurrences of {element} in the array: {count_occurrences(arr, element)} times")


if __name__ == "__main__":
    main()