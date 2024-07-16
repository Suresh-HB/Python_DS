'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Program to checking the element frist and last value equality
'''

def findStrLenCheckFristLast():
    """
    Description: Function to checking all the element frist and last value equality 
                 where length of the element is greater than or equal to 2
    Parameter:
    Return: 
    """


    List=['abc', 'xyz', 'aba', '1221']
    for ele in List:
        if len(ele)>2:
            if ele[0]==ele[-1]:
                print(f"The first and last characters of '{ele}' are equal.")
            else:
                print(f"The first and last characters of '{ele}' are not equal.")
                


def main():
    findStrLenCheckFristLast()

if __name__ == '__main__':
    main()