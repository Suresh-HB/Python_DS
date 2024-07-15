'''
@Author: Suresh
@Date: 2024-07-11 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : To identify and print the unique values from the given list dictionary.
'''


def findUniqueValue(x):
    """
    Description : Function to iterating the every key value pair in the list dictionary 
    and every value adding into set this ensures the uniqueness 
    Parameter: 
        x: taking x as a list dictionary input into the function 
    Return:
        uniqueValue: returns the set formatted uniqe values
    """


    uniqueValue=set()
    for i in x:
        for value in i.values():
            uniqueValue.add(value)
    return uniqueValue    


def main():
    x= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    res=findUniqueValue(x)
    print(res)


if __name__ == '__main__':
    main()