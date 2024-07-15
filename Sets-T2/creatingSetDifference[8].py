'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Program to create set Difference
'''



def setDifference():
    """
    Description: Function to finding the difference of elements
                 from multiple of sets
    Parameter: 
    Return: 
    """
        
    set1= {10,20,50,64,89,7,36,54,45}
    set2= {45,78,65,95,24,7,20,10,64}
    z = set1.difference(set2)
    print(z)


def main():
    setDifference()


if __name__ == '__main__':
    main()