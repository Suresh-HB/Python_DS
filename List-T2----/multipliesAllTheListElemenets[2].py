'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Program to multiplies with  all the elements in the list
'''


def sumListElements(list1): 
    """
    Description: Function to multiplies all the elements present in the given list 
    Parameter: Function to taking the list (list1) as a parameter
    Return: 
    """


    mul=1
    for ele in list1:
        mul=mul*ele
    print(mul," ---> after multiplies with allthe given list")


def main():
    list1=[10,20,30,40,50,60,70,80,90]
    sumListElements(list1) 


if __name__ == '__main__':
    main()