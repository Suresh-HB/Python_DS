'''

@Author: Suresh
@Date: 2024-07-16 
@Last Modified by: Suresh
@Last Modified: 2024-07-16 
@Title : Python program to replace all the frist occurrrene to $.

'''


def replace_char(s):
    
    """
    Description : Function to replace the all frist occurrence in to given character.
    Parameter :
        s : is the original string in to the function for replace the occurrences.
    Return: 
       mstr : returning after replace with specified character
    """


    if len(s) == 0:
        return s
    
    fChar = s[0]
    mstr = fChar + s[1:].replace(fChar, '$')

    return mstr


def main():

    instr = "python programming"
    res = replace_char(instr)
    print(res) 


if __name__ == '__main__':
    main()
