'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Program to create set Symmetric diffrence
'''


def  symmetric_diff():
    """
    Description: Function to finding the Symmetric diffrence between two sets
    Parameter: 
    Return: 
    """
        
    set1= {10,20,50,64,89,7,36,54,45}
    set2= {45,78,65,95,24,7,20,10,64}
    z=set1.symmetric_difference(set2)
    print(z)


def main():
    symmetric_diff()


if __name__ == '__main__':
    main()
