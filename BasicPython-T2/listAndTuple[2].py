'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Python program to conver list into tuple
'''


numbers_string = input("Enter comma-separated numbers: ")
number_list = numbers_string.split(',')
number_tuple = tuple(number_list)
print("List:", number_list)
print("Tuple:", number_tuple)
