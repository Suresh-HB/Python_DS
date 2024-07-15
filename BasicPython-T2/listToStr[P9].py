'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Python program to input converted back to string formate
'''

def lstr(lst):
 
 print(type(lst)," Before  converting --->",lst)
 names=lst.split()
 str="".join(names)
 
 print(type(lst)," after converting ---> ",str)
 

def main():
   lst=input("Enter the list of names")
   lstr(lst)

if __name__ == '__main__':
   main()


