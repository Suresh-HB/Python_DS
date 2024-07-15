'''
@Author: Suresh
@Date: 2024-07-11 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Python program to nested list.
'''


def list_to_nested_dict(keys_list, value):
    result = {}
    current_dict = result
    
    for key in keys_list[:-1]:
        current_dict[key] = {}
        current_dict = current_dict[key]
    
    current_dict[keys_list[-1]] = value
    
    return result

keys_list = ['A', 'B', 'C']
value = 10

nested_dict = list_to_nested_dict(keys_list, value)
print("Nested Dictionary:")
print(nested_dict)
