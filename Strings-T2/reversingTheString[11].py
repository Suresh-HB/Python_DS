'''

@Author: Suresh
@Date: 2024-07-16 
@Last Modified by: Suresh
@Last Modified: 2024-07-16 
@Title : Python program to reverse the given string.

'''


def reversing(str):
    
    """
    Description : Function to reversing the given string.
    Parameter :
        str : original string that will be reversing.
    Return: 
    """

    rev=str[::-1]
    print("After reversing--->",rev)


def main():
    
    str=input("Enter the string for reversing : ")
    print("Before revesing--->",str)
    reversing(str)


if __name__ == '__main__':
    main()