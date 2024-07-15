'''
@Author: Suresh
@Date: 2024-07-12 
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Python program to check multiple keys exists in a dictionary.
'''


def checkKeys(keys, my_dict):
    """
    Description: Function to check wether multiples keys present in the dictionary or not
    Parameter: 
        keys, my_dict : Function taking keys and dictionary as a input
    Return:
       True or False : returning the bool value based on the key presence
    """


    for key in keys:
        if key not in my_dict:
            return False
    return True


def main():
    my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    check1 = ['name', 'age']
    check2 = ['name', 'address']
    res1=checkKeys(check1,my_dict)
    res2=checkKeys(check2,my_dict)
    print(res1)
    print(res2)


if __name__ =='__main__':
    main()