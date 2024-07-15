'''
@Author: Suresh
@Date: 2024-07-11 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Taking user input as a key value pairs and store it into a dictionary
'''

def addDictionary():
    """
    Description: Function to store the user inputs key value pairs
    Parameter: 
        d, ascending=True : function taking parameters dictionary and bool value for sorting based on input
    Return:
       sorted_dict: returning the (ASC or DSC) sorted dictionary  
    """


    size =int(input("Enter the size of the dictionary\n"))
    dict1={}
    for i in range(size):
        key=int(input(f"Enter key : "))
        value=input(f"Enter value for key {key} = ")
        dict1[key]=value
    return dict1

def main():
    d1=addDictionary()
    print(d1)


if __name__ == '__main__':
    main()