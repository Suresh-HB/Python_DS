'''
@Author: Suresh
@Date: 2024-07-13
@Last Modified by: Suresh
@Last Modified: 2024-07-13 
@Title : Python program to find the repeated items of a tuple.
'''


from collections import Counter

def find_repeated_items(t):   
    """
    Description: Function to identify the elements which are repeatedly present in the tuple.
    Parameter: 
        t : Function taking the parameter as a tuple.
    Return: 
        repeated_items : Function returning the repeated values as a list
    """


    counts = Counter(t)
    repeated_items = [item for item, count in counts.items() if count > 1]
    
    return repeated_items


def main():
    my_tuple = (1, 2, 2, 3, 4, 4, 4, 5)
    repeated_items = find_repeated_items(my_tuple)
    print("Original Tuple:", my_tuple)
    print("Repeated Items:", repeated_items)


if __name__ == '__main__':
    main()
