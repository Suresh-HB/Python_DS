'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Printing the given dictionary key value pairs in table form.
'''


def table_dictionary(dict1):
    """
    Description: Function to printing the given dictionary key value pairs in the form of table view to user 
    Parameter: 
        dict1: function taking given dictionary as a parameters into function
    Return:  
    """

    print("KEY\t\tValue")
    print("---------------------------")
    for key,value in dict1.items():
        print(f"{key}: \t\t {value}")
    print("---------------------------")


def main():

    dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    table_dictionary(dict1)


if __name__ =='__main__':
    main()