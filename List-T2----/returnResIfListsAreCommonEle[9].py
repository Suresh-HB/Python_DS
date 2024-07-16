'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : a Python function that takes two lists and returns True if they have at
least one common member
'''
def common_data(list1, list2):
    """
    Description: Function taking the two input lists and compare their elements 
                equality and gives result 
    Parameter:
        list1, list2 : Function to taking as a parameter for comparision
    Return: 
        result : (True or False) after checking the equality of the elements from both the lists 
    """
   
   
    result = False
 
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result 
                 
    return result
     
def main():

    a = [1, 2, 3, 4, 5]
    b = [5, 6, 7, 8, 9]
    res=common_data(a, b)
    print(res)
    
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 8, 9]
    rest=common_data(x, y)
    print(rest)


if __name__ == '__mai __':
    main()