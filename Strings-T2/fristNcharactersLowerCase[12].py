'''

@Author: Suresh
@Date: 2024-07-16 
@Last Modified by: Suresh
@Last Modified: 2024-07-16 
@Title : Python program to convert the begining characters of the string into lower case.

'''


def lowercase_conversion(lc,str):
    
    """
    Description : Function to convert the begining characters of the string into lower case.
    Parameter :
        lc : is the number of charaters want to be in lower case at begining 
        str : original string that will be case manipulating at begining of the string charaters.
    Return: 
    """

    if lc<len(str):

        res=str[0:lc].lower()+str[lc:]
        print(res)
    else :
        print(f"Entered number {lc} is out of range")


def main():


    str=input("Enter the string : ")
    print("you entered string ", str)

    lc=input("Enter how much character should be in lower case at begining : ")
    lc=int(lc)

    lowercase_conversion(lc,str)


if __name__ == '__main__':
    main()