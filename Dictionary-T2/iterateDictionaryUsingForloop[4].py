'''
@Author: Suresh
@Date: 2024-07-11 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Taking User input dictionary and iterating the key values pairs 
'''

def traversingDictionary():
    """
    Description : Function to take User input dictionary size,keys,values 
        and iterating the key values pairs using for loop 
    Parameter: 
    Return:
        dict1 : returning the concatinated new dictionary
    """

    
    size =int(input("Enter the size of the dictionary\n"))
    dict1={}
    for i in range(size):
        key=int(input(f"Enter key : "))
        value=input(f"Enter value for key {key} = ")
        dict1[key]=value
    return dict1


def main():
    dict1=traversingDictionary()
    for key, value in dict1.items(): # items method returns key pairs 
        print(f"key : {key}--->value = {value}")
    

if __name__ == '__main__':
    main()