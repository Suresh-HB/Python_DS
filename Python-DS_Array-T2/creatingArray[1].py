'''

@Author: Suresh
@Date: 2024-07-11
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Creating and iterating array elements

'''

import array


def arrayCreating():
    """
    Description: Function to iterates the elements present in the Array and prints based on indexs
    Parameter: 
    Return:
    """
    
    arr=array.array('i',[10, 20, 30, 40, 50])
    
    print("Elements of the array based on index:")
    for i in range(len(arr)):
        print(f"Element at index {i} = {arr[i]}")


def main():
    arrayCreating()
   

if __name__ == '__main__':
    main()
