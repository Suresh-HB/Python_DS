'''

@Author: Suresh
@Date: 2024-07-16 
@Last Modified by: Suresh
@Last Modified: 2024-07-16 
@Title : Python program to add suffix to given string.

'''



def addString(s):
    
    """
    Description : Function to adding the extra required character at ending of given string.
    Parameter :
        s : origignal string for adding extra required characters.
    Return: 
        s+'ing' : returns the string after adding required characters at ending of the string. 
    """


    if len(s)<3:
        return s
    
    if s.endswith('ing'):
        return s+'ly'
    else:
        return s+'ing'


def main():
    
    str="pyhton programing"
    res=addString(str)
    print(res)


if __name__ == '__main__':
    main()