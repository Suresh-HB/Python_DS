'''

@Author: Suresh
@Date: 2024-07-16 
@Last Modified by: Suresh
@Last Modified: 2024-07-16 
@Title : Python program to converting user input into Upper and lower case and display .

'''


def caseConversion(s):

    """
    Description: Function to converts the input as upper and lower case .
    Parameter:
       s: Function taking (s) as an  incoming parameter in to the function.
    Return: 
    """


    up=s.upper()
    lw=s.lower()
    print(up)
    print(lw)


def main():

    str=input("Enter one sentence : ")
    caseConversion(str)


if __name__ == '__main__':
    main()