'''
@Author: Suresh
@Date: 2024-07-12 
@Last Modified by: Suresh
@Last Modified: 2024-07-12
@Title : Count the dictionary items value that is a list
'''


def countListValues(d):
    """
    Description : Function to takes input as a dictionary and find out length of the items value list
    Parameter:
        d: dictionary as a input to this function
    Return:
        count : returning the count of the dictionary values of list
    """


    count=0

    for c in d:
        if isinstance(d[c],list):
            count+=len(d[c])
    return count


def main():
    
    d = {'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],'B' : 34,'C' : 12,'D' : [7, 8, 9, 6, 4] }
    count=countListValues(d)
    print(count)
    
    
if __name__ == '__main__':
    main()