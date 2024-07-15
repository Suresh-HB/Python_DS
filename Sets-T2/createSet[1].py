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
                 the user values into the set 
    Parameter: Function taking the size as a intput parameter 
    Return: 
    """


# manually creating the set like this --->my_set={10,20,30,40}

    my_set=set()

    for i in range(size):      
        a=input(f"Enter the value for size {i+1}--->")
        my_set.add(a)
    print(type(my_set))
    print(my_set)


def main():
    size=int(input("Enter the size of the set : "))
    createSet(size)


if __name__ == '__main__':
    main()

