'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Adding members in to already existing set
'''


def addMembers(my_set):
    """
    Description: Function to adding the user members in to already existing set 
    Parameter: Function taking the existing set (my_set) as a parameter
    Return: 
    """

    ele=int(input("Enter how much element you want to add : "))
    print(f"Your willing to add {ele} elements in to already existing set")

    for i in range(ele):      
        a=input(f"Enter element for --->{i+1} : ")
        my_set.add(a)
    print(my_set)


def main():
    my_set={10,20}
    addMembers(my_set)


if __name__ == '__main__':
    main()

