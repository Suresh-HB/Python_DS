'''
@Author: Suresh
@Date: 2024-07-12
@Last Modified by: Suresh
@Last Modified: 2024-07-12 
@Title : Remove the specific element from the Set
'''


def removeElement(ele,set1):
    """
    Description: Function to remove the specified element from existing set 
    Parameter: Function takes element for delete, set1 and ele as a parameter 
    Return: 
    """

    if ele in set1:
        set1.remove(ele)
    print()



def main():
    set1={10,20,60,40,8,296,56,45}
    print(set1)
    ele=int(input("Enter which element you want to remove from this set : "))
    removeElement(ele,set1)


if __name__ == '__main__':
    main()