'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Python program to count the values associated with key in a
dictionary.
'''


def countTrues(ld1):

    count=0
    for i in ld1:
        for value in i.values():
            if value=='True':
                count+=1
    return count


def main():
    """
    Description : Function to 
    Parameter: 
    Return: 
    """


    ld1= [{'id': 1, 'success': 'True', 'name': 'Lary'}, {'id': 2, 'success':'False', 'name': 'Rabi'}, {'id': 3, 'success': 'True', 'name': 'Alex'}]
    count=countTrues(ld1)
    print(count ,"Dictionaries have success as True ")


if __name__ == '__main__':
    main()