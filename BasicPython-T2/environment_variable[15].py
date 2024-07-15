'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-11 
@Title : Access Environment Variables
'''


import os

username = os.getenv('USERNAME')
print(f'Username: {username}')

env_vars = os.environ

print('\nAll Environment Variables:')

for key, value in env_vars.items():
    print(f'{key}: {value}')
