'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Creating the set using user input
'''


def createSet(size):
    """
    Description: Function to creates the set based on the provided size and store 
                 the user values into the set and iterating the set using for loop and printing
    Parameter: Function taking the size as a intput parameter 
    Return: 
    """


    my_set=set()

    for i in range(size):      
        a=input(f"Enter the value for size {i+1}--->")
        my_set.add(a)
    
    
    for x in my_set:
        print(x)


def main():
    size=int(input("Enter the size of the set : "))
    createSet(size)


if __name__ == '__main__':
    main()