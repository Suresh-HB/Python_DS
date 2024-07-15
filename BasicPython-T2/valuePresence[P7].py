'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Python program for calender
'''

def major(v1,v2):
    lst1=[1, 5, 8, 3] 
    lst2= [1, 5, 8, 3] 
    if  v1 in lst1:
        print(f"The specified element ,({v1}) is  present in the list-1 ")
    else :
        print(f"The specified element ,({v1}) is not present in the list-1 ")
    
    if  v2 in lst1:
        print(f"The specified element ,({v2}) is  present in the list-1 ")
    else :
        print(f"The specified element ,({v2}) is not present in the list-1 ")


v1=int(input("Enter value for check the value is present in the list1 or not\n"))
v2=int(input("Enter value for check the value is present in the list2 or not\n"))
major(v1,v2)